# Generated by Django 4.2 on 2023-05-01 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('year', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('role', models.CharField(choices=[('Principal', 'Principal'), ('Wise_Principal', 'wise Principal'), ('Class_Teacher', 'Class Teacher'), ('Other', 'Other')], max_length=50, null=True)),
                ('classRoom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sclmain.classroom')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sclmain.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('std_index_no', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('std_ID', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Other')], max_length=50, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('b_date', models.DateTimeField(null=True)),
                ('father_name', models.CharField(max_length=200, null=True)),
                ('mother_name', models.CharField(max_length=200, null=True)),
                ('comment', models.TextField(null=True)),
                ('classRoom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sclmain.classroom')),
            ],
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(choices=[('TERM1', 'TERM 1'), ('TERM2', 'TERM 2'), ('TERM3', 'TERM 3')], max_length=50, null=True)),
                ('marks', models.IntegerField()),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sclmain.student')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sclmain.subject')),
            ],
        ),
    ]