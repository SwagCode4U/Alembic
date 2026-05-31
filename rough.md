CREATE DATABASE IF NOT EXISTS learnsmart;
USE learnsmart;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    date_of_birth DATE,
    class_name VARCHAR(20)
);

CREATE TABLE courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    code VARCHAR(20) UNIQUE,
    credits INT DEFAULT 3
);


INSERT INTO students (name, email, phone, date_of_birth, class_name) VALUES
('Rahul Sharma', 'rahul@email.com', '9876543210', '2010-05-15', '5A'),
('Priya Patel', 'priya@email.com', '9876543211', '2011-08-20', '5A'),
('Amit Singh', 'amit@email.com', '9876543212', '2010-12-10', '5B');
INSERT INTO courses (name, code, credits) VALUES
('Mathematics', 'MATH101', 4),
('Science', 'SCI101', 4);



SELECT '✅ students:' AS info, COUNT(*) AS count FROM students
UNION ALL
SELECT '✅ courses:', COUNT(*) FROM courses;





DemoAlembic/
├── .env
├── requirements.txt
├── main.py
├── manual_setup.sql
├── alembic.ini              ← Will create after "alembic init"
├── alembic/                 ← Will create after "alembic init"
├── app/
│   ├── config.py
│   ├── database.py
│   └── models/ (20 files)


pip install alembic
alembic init alembic

alembic.ini ---> config (DB URL batana hai)

alembic/env.py --->

alembic/versions/ ---> MG store karenge


alembic current         # DB se Connection Alembic hua ke nahi
DB connection test      # 


alembic revision --autogenerate -m "create_all_20_tables"
# Migration


# Autogenerate
alembic revision --autogenerate -m "add_address_to_students"


cat alembic/versions/d2dd4f1e4925_add_address_to_students.py         
#So We can Read the File



def upgrade():
    op.add_column("students",
        sa.Column("address", sa.String(200), nullable=True))

def downgrade():
    op.drop_column("students", "address")

alembic upgrade head    




# 🧪 VERIFY: Data safe??
mysql -u root -pApple%401234 learnsmart -e "DESCRIBE students;"
```

**Output:**
```
+------------+--------------+------+-----+---------+----------------+
| Field      | Type         | Null |     | Default |                |
+------------+--------------+------+-----+---------+----------------+
| id         | int          | NO   | PRI | NULL    | auto_increment |
| name       | varchar(100) | NO   |     | NULL    |                |
| email      | varchar(100) | YES  | UNI | NULL    |                |
| phone      | varchar(20)  | YES  |     | NULL    |                |
| date_of_birth | date      | YES  |     | NULL    |                |
| class_name | varchar(20)  | YES  |     | NULL    |                |
| address    | varchar(200) | YES  |     | NULL    | ← 🔥 NAYA!     |
+------------+--------------+------+-----+---------+----------------+

alembic history -v



(venv) ➜  DemoAlembic alembic history   
0ff61a0b9b16 -> 9efaac1c83fb (head), enlarge_phone_column
4dbe53e15cf5 -> 0ff61a0b9b16, enlarge_phone_column
96291d49a1bc -> 4dbe53e15cf5, create_homework_help_table
d2dd4f1e4925 -> 96291d49a1bc, create_homework_help_table
2bdd9aadc755 -> d2dd4f1e4925, add_address_to_students
<base> -> 2bdd9aadc755, create_all_20_tables
(venv) ➜  DemoAlembic 





# === DAILY USE ===
alembic revision --autogenerate -m "description"   # Change detect + file banao
alembic upgrade head                                 # Apply all pending
alembic downgrade -1                                 # Ek step peeche

# === INFO ===
alembic current              # Kaunsa migration abhi hai?
alembic history              # Saari migrations

# === SAFE ===
alembic upgrade head --sql   # Sirf SQL dekho, apply mat karo



# === NEW FEATURE ===
# 1. Model banao (app/models/*.py)
# 2. env.py mein import karo
# 3. alembic revision --autogenerate -m "new_feature"
# 4. alembic upgrade head
```
