# Generated by Django 4.2 on 2023-05-02 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sclmain', '0007_remove_student_mark1_marks_student_alter_marks_marks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sclmain.student'),
        ),
    ]
