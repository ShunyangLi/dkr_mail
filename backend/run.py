from app import app
import api.mail_handling
from utils.schedule_work import scheduler

if __name__ == '__main__':
    scheduler.init_app(app)
    scheduler.start()
    app.run(debug=True)
