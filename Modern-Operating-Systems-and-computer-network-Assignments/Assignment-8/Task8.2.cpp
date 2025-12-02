#include <iostream>
#include <iomanip>
using namespace std;

struct Process {
    string pid;
    int at, bt, ct, tat, wt;
    bool completed;
};

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
        p[i].completed = false;
        cout << endl;
    }

    int completed = 0;
    int time = 0;
    int totalTAT = 0, totalWT = 0;

    cout << "\nGANTT CHART: \n";

    while (completed != n) {

        int idx = -1;
        int minBT = 1e9;

        // Select process with minimum burst time among arrived processes
        for (int i = 0; i < n; i++) {
            if (p[i].at <= time && !p[i].completed) {
                if (p[i].bt < minBT) {
                    minBT = p[i].bt;
                    idx = i;
                }
            }
        }

        // If no process has arrived → CPU idle
        if (idx == -1) {
            time++;
            continue;
        }

        // Execute selected process
        cout << "| " << p[idx].pid << " ";

        time += p[idx].bt;
        p[idx].ct = time;
        p[idx].tat = p[idx].ct - p[idx].at;
        p[idx].wt  = p[idx].tat - p[idx].bt;

        p[idx].completed = true;
        completed++;

        totalTAT += p[idx].tat;
        totalWT += p[idx].wt;
    }

    cout << "|\n\n";

    // Print results
    cout << "\nSJF Scheduling Results:\n";
    cout << "---------------------------------------------------------------\n";
    cout << left << setw(10) << "PID"
         << setw(15) << "AT"
         << setw(15) << "BT"
         << setw(15) << "CT"
         << setw(15) << "TAT"
         << setw(15) << "WT" << endl;
    cout << "---------------------------------------------------------------\n";

    for (int i = 0; i < n; i++) {
        cout << left << setw(10) << p[i].pid
             << setw(15) << p[i].at
             << setw(15) << p[i].bt
             << setw(15) << p[i].ct
             << setw(15) << p[i].tat
             << setw(15) << p[i].wt << endl;
    }

    cout << "---------------------------------------------------------------\n";
    cout << "Average Turnaround Time = " << (float)totalTAT / n << endl;
    cout << "Average Waiting Time    = " << (float)totalWT / n << endl;

    return 0;
}
