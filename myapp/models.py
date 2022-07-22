from django.db import models


class User(models.Model):
    user_name = models.CharField(verbose_name='用户名', max_length=10, unique=True)
    user_password = models.IntegerField(verbose_name='用户密码')
    user_type = models.IntegerField(verbose_name='用户类型', choices=((1, '管理员'), (2, '教师'), (3, '学生')), default=3)

    def __str__(self):
        return self.user_name


class Teacher(models.Model):
    the_course = models.CharField(verbose_name='课程名', max_length=20, unique=True)
    teacher_name = models.ForeignKey(verbose_name='老师名', to="User", to_field="user_name", on_delete=models.CASCADE)
    course_pass = models.IntegerField(verbose_name='课程状态', choices=((1, '待审核'), (2, '通过'), (3, '不通过')), default=1)

    def __str__(self):
        return self.the_course


class ChoiceQuestion(models.Model):
    question = models.CharField(verbose_name='问题', max_length=200)
    optionA = models.CharField(verbose_name="选项A", max_length=50)
    optionB = models.CharField(verbose_name="选项B", max_length=50)
    optionC = models.CharField(verbose_name="选项C", max_length=50)
    optionD = models.CharField(verbose_name="选项D", max_length=50)
    answer = models.CharField(verbose_name="正确答案", choices=(('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')),
                              default='A', max_length=2)
    its_course = models.ForeignKey(verbose_name="所属课程", to="Teacher", to_field="the_course", on_delete=models.CASCADE)


class TFQuestion(models.Model):
    question = models.CharField(verbose_name='问题', max_length=200)
    answer = models.BooleanField(verbose_name='正确答案')
    its_course = models.ForeignKey(verbose_name="所属课程", to="Teacher", to_field="the_course", on_delete=models.CASCADE)


class Completion(models.Model):
    question = models.CharField(verbose_name='问题', max_length=200)
    answer = models.CharField(verbose_name='正确答案', max_length=20)
    its_course = models.ForeignKey(verbose_name="所属课程", to="Teacher", to_field="the_course", on_delete=models.CASCADE)


class Student(models.Model):
    course = models.ForeignKey(verbose_name='课程名', to='Teacher', to_field='the_course', on_delete=models.CASCADE)
    student_name = models.ForeignKey(verbose_name='学生名', to="User", to_field="user_name", related_name='s_name',
                                     on_delete=models.CASCADE)
    teacher_name = models.ForeignKey(verbose_name='老师名', to='User', to_field='user_name', related_name='t_name',
                                     on_delete=models.CASCADE)
    grade = models.CharField(verbose_name='成绩', max_length=5, blank=True, null=True)


class Anw(models.Model):
    course = models.ForeignKey(verbose_name='课程名', to='Teacher', to_field='the_course', on_delete=models.CASCADE)
    student_name = models.ForeignKey(verbose_name='学生名', to="User", to_field="user_name", related_name='stu_name',
                                     on_delete=models.CASCADE)
    question = models.CharField(verbose_name='问题', max_length=200)
    answer = models.CharField(verbose_name='正确答案', max_length=20)
    stu_anw = models.CharField(verbose_name='学生答案', max_length=20)
    tof = models.BooleanField(verbose_name='是否正确')
    type_of_questions = models.CharField(verbose_name='题目类型', max_length=20)
