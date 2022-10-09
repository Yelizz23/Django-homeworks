rom django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='articlescope',
            name='unique_true_is_main',
        ),
        migrations.AddConstraint(
            model_name='articlescope',
            constraint=models.UniqueConstraint(condition=models.Q(('is_main', True)), fields=('is_main', 'article'),
                                               name='unique_true_is_main'),
        ),
    ]