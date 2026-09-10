# Bank Account Simulator V2

A bank account simulator built in Python, with real data persistence using a MySQL database. This is an evolution of the V1 project, which only kept data in memory — in this version, accounts and transactions are saved permanently.

## Features

- Create bank accounts
- Deposit and withdraw, with balance validation
- Transaction history (statement) per account
- Balance lookup straight from the database
- Data persistence via MySQL (data survives after the program closes)

## Technologies used

- **Python** — application logic (object-oriented)
- **MySQL** — relational database
- **mysql-connector-python** — connection between Python and MySQL
- **python-dotenv** — credential management via environment variables

## Database structure

The project uses two related tables:

**`contas`**
| Column | Type | Description |
|---|---|---|
| id | INT (PK, auto-increment) | Unique account identifier |
| nome | VARCHAR(100) | Account holder's name |
| saldo | DECIMAL(10,2) | Current account balance |

**`transacoes`**
| Column | Type | Description |
|---|---|---|
| id | INT (PK, auto-increment) | Unique transaction identifier |
| conta_id | INT (FK → contas.id) | Account the transaction belongs to |
| tipo | VARCHAR(20) | Transaction type ('deposito' or 'saque') |
| valor | DECIMAL(10,2) | Amount moved |
| data_hora | DATETIME | Transaction date and time (auto-filled) |

## How to run the project

### Requirements

- Python 3 installed
- MySQL Server installed and running

### Steps

1. Clone this repository:
```
git clone <repository-url>
```

2. Install the dependencies:
```
pip install mysql-connector-python python-dotenv
```

3. Create the database in MySQL:
```sql
CREATE DATABASE simuladorv2;
```

4. Create a `.env` file in the project root with your MySQL credentials:
```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password_here
DB_PORT=3306
```

5. Run the program:
```
python __main__.py
```

## Author

Cauã Justiniano
