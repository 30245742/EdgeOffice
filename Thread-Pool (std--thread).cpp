#include <filesystem>
#include <thread>
#include <mutex>
#include <queue>
#include <openssl/sha.h>

std::queue<std::filesystem::path> work_q;
std::mutex q_mutex;

void worker() {
    while (true) {
        std::filesystem::path p;
        {
            std::lock_guard<std::mutex> lock(q_mutex);
            if (work_q.empty()) return;
            p = work_q.front();
            work_q.pop();
        }
        // hash file (SHA-256)
    }
}