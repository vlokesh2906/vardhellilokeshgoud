#include <iostream>
#include <iomanip>
using namespace std;

struct Process {
    string pid;
    int at, bt, ct, tat, wt;
};

// Sort by Arrival Time
void sortByArrival(Process p[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (p[j].at > p[j+1].at) {
                swap(p[j], p[j+1]);
            }
        }
    }
}

int main() {
    int n;
    cout << "Enter number of processes: ";
    cin >> n;

    Process p[n];

    for (int i = 0; i < n; i++) {
        cout << "Enter Process ID: ";
        cin >> p[i].pid;
        cout << "Arrival Time: ";
        cin >> p[i].at;
        cout << "Burst Time: ";
        cin >> p[i].bt;
        cout << endl;
    }

    // Sort by arrival time
    sortByArrival(p, n);

    int time = 0;
    int totalTAT = 0, totalWT = 0;

    for (int i = 0; i < n; i++) {

        // If CPU is idle
        if (time < p[i].at) {
            time = p[i].at;
        }

        // Completion time
        time += p[i].bt;
        p[i].ct = time;

        // Turnaround time and waiting time
        p[i].tat = p[i].ct - p[i].at;
        p[i].wt = p[i].tat - p[i].bt;

        totalTAT += p[i].tat;
        totalWT += p[i].wt;
    }

    // Display result
    cout << "\nFCFS Scheduling Results:\n";
    cout << "-------------------------------------------------------------\n";
    cout << left << setw(10) << "PID"
         << setw(15) << "AT"
         << setw(15) << "BT"
         << setw(15) << "CT"
         << setw(15) << "TAT"
         << setw(15) << "WT" << endl;
    cout << "-------------------------------------------------------------\n";

    for (int i = 0; i < n; i++) {
        cout << left << setw(10) << p[i].pid
             << setw(15) << p[i].at
             << setw(15) << p[i].bt
             << setw(15) << p[i].ct
             << setw(15) << p[i].tat
             << setw(15) << p[i].wt << endl;
    }

    cout << "-------------------------------------------------------------\n";
    cout << "Total Turnaround Time = " << totalTAT << endl;
    cout << "Total Waiting Time    = " << totalWT << endl;
    cout << "Average TAT = " << (float)totalTAT/n << endl;
    cout << "Average WT  = " << (float)totalWT/n << endl;

    return 0;
}
