# Generated by Django 4.0.1 on 2022-01-26 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_question_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='A', max_length=2, verbose_name='正确答案'),
        ),
        migrations.AlterField(
            model_name='question',
            name='its_course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.teacher', to_field='the_course', verbose_name='所属课程'),
        ),
        migrations.AlterField(
            model_name='question',
            name='optionA',
            field=models.CharField(max_length=50, verbose_name='选项A'),
        ),
        migrations.AlterField(
            model_name='question',
            name='optionB',
            field=models.CharField(max_length=50, verbose_name='选项B'),
        ),
        migrations.AlterField(
            model_name='question',
            name='optionC',
            field=models.CharField(max_length=50, verbose_name='选项C'),
        ),
        migrations.AlterField(
            model_name='question',
            name='optionD',
            field=models.CharField(max_length=50, verbose_name='选项D'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(max_length=200, verbose_name='问题'),
        ),
    ]
