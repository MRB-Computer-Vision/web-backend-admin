from app.main import db
from app.main.models.exam import Exam, ExamFile
from app.main.models.medical_record import MedicalRecord
class ExamRepository:

  def __init__(self):
    self.exam = Exam()

  def save(self, data):
    try:
        self.exam.type = data['type']
        self.exam.medical_record = self.get_medical_record(data)
        self.exam.exam_files = self.initialize_exam_files(data['exam_files'])
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

  def get_medical_record(self, data):
    error_message = "number attribute required"
    if not self.is_medical_record_number_present(data):
        raise Exception(error_message)
    medical_record = MedicalRecord.query.filter_by(number=str(data['number'])).first()
    if not medical_record:
        medical_record = MedicalRecord(data['number'])
    return medical_record

  def is_medical_record_number_present(self, data):
      return 'number' in data.keys() and data['number']