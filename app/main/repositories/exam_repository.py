from app.main import db
from app.main.models.exam import Exam, ExamFile

class ExamRepository:

  def __init__(self):
    self.exam = Exam()

  def save(self, data):
    try:
        self.exam.type = data['type']
        exam_files = self.initialize_exam_files(data['exam_files'])
        self.exam.exam_files = exam_files
        db.session.add(self.exam)
        #db.session.refresh(self.exam)
        db.session.commit()
        return self.exam
    except Exception as e:
        return e

  def update_exam_result(self, result):
    try:
        self.exam.result = result
        self.exam.status = 'processed'
        db.session.add(self.exam)
        db.session.commit()
        return self.exam
    except Exception as e:
        return e

  def update(self, _id, data):
    try:
      #FIXME: Need to study how to update multiple fields
      exam = Exam.query.filter_by(id=_id).first()
      exam.result = data['result']
      db.session.commit()
      return self.exam
    except Exception as e:
      return e

  def initialize_exam_files(self, exam_files_params):
      exam_files = []
      for exam_file_param in exam_files_params:
          exam_files.append(ExamFile(file_path=exam_file_param['file_path']))
      return exam_files