from taskmanager import db


class category(db.Model):
    id = db.column(db.integer, primary_key=True)
    category_name = db.Column(db.string(25), unique=True, nullable=False)
    tasks = db.relationship("Task", backref="category", cascade="all, delete", lazy=True    )

    def __repr__(self):
        return self.category_name


class Task(db.model):
    id = db.column(db.integer, primary_key=True)
    task_name = db.Column(db.string(50), unique=True. nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    category_id = db.Column(db.integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)


    def __repr__(self):
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )

