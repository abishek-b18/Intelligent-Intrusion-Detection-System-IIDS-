from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ThreatLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source_ip = db.Column(db.String(50))
    attack_type = db.Column(db.String(100))
    severity = db.Column(db.String(20))