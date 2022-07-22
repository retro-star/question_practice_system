# Generated by Django 4.0.1 on 2022-01-30 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_question_answer_alter_question_its_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.teacher', to_field='the_course', verbose_name='课程名'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user', to_field='user_name', verbose_name='学生名'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='course_pass',
            field=models.IntegerField(choices=[(1, '待审核'), (2, '通过'), (3, '不通过')], default=1, verbose_name='课程状态'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user', to_field='user_name', verbose_name='老师名'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='the_course',
            field=models.CharField(max_length=20, unique=True, verbose_name='课程名'),
        ),
    ]
