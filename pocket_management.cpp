#include<iostream>
#include<fstream>
#include <string>
#include <ctime>
#include <vector>
#include <algorithm>
#include <numeric> // Include the numeric header for accumulate

using namespace std;

struct Expense {
    string date;
    string description;
    double amount;
};

bool compareExpenses(const Expense& expense1, const Expense& expense2) {
    // Custom comparison function to sort expenses by date
    return expense1.date < expense2.date;
}

void saveExpensesToFile(const vector<Expense>& expenses) {
    ofstream file("expenses.txt");

    if (file.is_open()) {
        for (const auto& expense : expenses) {
            file << expense.date << "," << expense.description << "," << expense.amount << endl;
        }

        file.close();
        cout << "Expenses saved to file.\n";
    } else {
        cout << "Unable to open file for writing.\n";
    }
}

void loadExpensesFromFile(vector<Expense>& expenses) {
    expenses.clear();
    ifstream file("expenses.txt");

    if (file.is_open()) {
        string line;
        while (getline(file, line)) {
            Expense expense;
            size_t pos = line.find(',');
            expense.date = line.substr(0, pos);
            line.erase(0, pos + 1);

            pos = line.find(',');
            expense.description = line.substr(0, pos);
            line.erase(0, pos + 1);

            try {
                expense.amount = stod(line);
                expenses.push_back(expense);
            } catch (const std::invalid_argument& e) {
                cout << "Invalid expense amount: " << line << ". Skipping expense.\n";
            }
        }

        file.close();
        cout << "Expenses loaded from file.\n";
    } else {
        cout << "Unable to open file for reading.\n";
    }
}

void displayExpenses(const vector<Expense>& expenses, double salary, double balance) {
    cout << "Expenses:\n";
    cout << "-----------------------------------------------------\n";
    cout << "Date         | Description       | Amount ($)       \n";
    cout << "-----------------------------------------------------\n";

    for (const auto& expense : expenses) {
        cout << expense.date << " | " << expense.description << " | " << expense.amount << endl;
        cout << "-----------------------------------------------------\n";
    }

    cout << "Remaining balance from salary: $" << (salary - balance) << endl;
}

void searchExpensesByDate(const vector<Expense>& expenses, const string& date) {
    cout << "Expenses on " << date << ":\n";
    cout << "-----------------------------------------------------\n";
    cout << "Date         | Description       | Amount ($)       \n";
    cout << "-----------------------------------------------------\n";

    for (const auto& expense : expenses) {
        if (expense.date == date) {
            cout << expense.date << " | " << expense.description << " | " << expense.amount << endl;
            cout << "-----------------------------------------------------\n";
        }
    }
}

int main() {
    double salary;
    double balance = 0.0;
    int choice;
    double amount;
    string expenseDate;
    string expenseDescription;
    vector<Expense> expenses;

    loadExpensesFromFile(expenses);

    cout << "Enter your salary amount: ";
    cin >> salary;
    balance = salary;

  while (true) {
    cout << "Budget Management System\n";
    cout << "1. Add income\n";
    cout << "2. Add expense\n";
    cout << "3. Check balance\n";
    cout << "4. Display expenses\n";
    cout << "5. Search expenses by date\n";
    cout << "6. Save expenses to file\n";
    cout << "7. Start a new table for this month\n";
    cout << "8. Exit\n";
    cout << "Enter your choice: ";
    cin >> choice;

    switch (choice) {
        case 1:
            cout << "Enter the income amount: ";
            cin >> amount;
            balance += amount;
            cout << "Income added successfully.\n";
            break;
        case 2:
            cout << "Enter the expense amount: ";
            cin >> amount;
            if (balance >= amount) {
                balance -= amount;
                cout << "Enter the date of the expense (DD/MM/YYYY): ";
                cin >> expenseDate;
                cin.ignore();  // Ignore the newline character
                cout << "Enter a description of the expense: ";
                getline(cin, expenseDescription);

                Expense expense;
                expense.date = expenseDate;
                expense.description = expenseDescription;
                expense.amount = amount;

                expenses.push_back(expense);
                cout << "Expense added successfully.\n";
            } else {
                cout << "Insufficient balance to add the expense.\n";
            }
            break;
    case 3: {
                double totalExpenses = accumulate(expenses.begin(), expenses.end(), 0.0, [](double sum, const Expense& expense) {
                    return sum + expense.amount;
                });
                double remainingBalance = salary - totalExpenses;

                cout << "Remaining balance: " << (remainingBalance >= 0 ? "₹" : "-₹") << abs(remainingBalance) << endl;
                cout << "Calculation: ₹" << salary << " - ₹" << totalExpenses << " = " << (remainingBalance >= 0 ? "₹" : "-₹") << abs(remainingBalance) << endl;
                break;
            }

        case 4:
            sort(expenses.begin(), expenses.end(), compareExpenses);
            displayExpenses(expenses, salary, balance);
            break;
        case 5:
            cout << "Enter the date to search (DD/MM/YYYY): ";
            cin >> expenseDate;
            searchExpensesByDate(expenses, expenseDate);
            break;
        case 6:
            saveExpensesToFile(expenses);
            break;
        case 7:
            // Start a new table for this month
            expenses.clear();
            cout << "New table started for this month.\n";
            break;
        case 8:
            cout << "Exiting the program.\n";
            return 0;
        default:
            cout << "Invalid choice. Please try again.\n";
    }

    cout << "\n";
}
return 0;
}
