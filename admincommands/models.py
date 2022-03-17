from django.db import models
from contextlib import redirect_stdout, redirect_stderr
from django.db import connection
from django.core.management import execute_from_command_line
from django.utils import timezone
from django.conf import settings
import io


class CommandRunInstance(models.Model):
    runner_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )

    command = models.TextField()
    stdout = models.TextField(blank=True)
    stderr = models.TextField(blank=True)
    exception = models.TextField(blank=True)

    executed_at = models.DateTimeField(auto_now_add=True, editable=False)
    finished_at = models.DateTimeField(null=True, editable=False)

    def save(self, *args, **kwargs):
        if self.id:
            # dont care about regular updates
            return super().save(*args, **kwargs)
        # here means the object is freshly created.
        with redirect_stdout(io.StringIO()) as f_out:
            with redirect_stderr(io.StringIO()) as f_err:
                try:
                    execute_from_command_line(['./manage.py'] + self.command.split(' '))
                except (Exception, SystemExit) as e:
                    self.exception = str(e)
                self.finished_at = timezone.now()
                # restart the db connection required for db related commands that
                # close the db connection (like migrate)
                connection.connect()

                self.stdout = f_out.getvalue()
                self.stderr = f_err.getvalue()

        return super().save(*args, **kwargs)

    def __str__(self):
        return 'ID {} {} (ran at {})'.format(self.id, self.command, self.executed_at)