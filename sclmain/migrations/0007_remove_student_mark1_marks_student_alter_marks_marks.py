# Generated by Django 4.2 on 2023-05-02 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sclmain', '0006_remove_marks_student_student_mark1_alter_marks_marks_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='mark1',
        ),
        migrations.AddField(
            model_name='marks',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sclmain.student'),
        ),
        migrations.AlterField(
            model_name='marks',
            name='marks',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
