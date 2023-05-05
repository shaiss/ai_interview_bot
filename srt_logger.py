import datetime

class SRTLogger:
    def __init__(self):
        self.entries = []

    def log_entry(self, speaker, content, start_time, end_time):
        self.entries.append({
            "speaker": speaker,
            "content": content,
            "start_time": start_time,
            "end_time": end_time,
        })

    def save_transcript(self, filename):
        with open(filename, "w") as f:
            index = 1
            for entry in self.entries:
                start = entry["start_time"].strftime("%H:%M:%S,%f")[:-3]
                end = entry["end_time"].strftime("%H:%M:%S,%f")[:-3]
                f.write(f"{index}\n{start} --> {end}\n{entry['speaker']}: {entry['content']}\n\n")
                index += 1
