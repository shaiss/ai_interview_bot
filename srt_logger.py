# srt_logger.py
import datetime


class SRTLogger:

  def __init__(self):
    self.entries = []

  def log_entry(self, speaker, message, start_time, end_time):
    self.entries.append({
      "speaker": speaker,
      "message": message,
      "start_time": start_time,
      "end_time": end_time
    })

  def _format_time(self, time_obj):
    return str(time_obj).replace(".", ",")

  def save_transcript(self, file_path):
    with open(file_path, "w") as f:
      for index, entry in enumerate(self.entries, 1):
        f.write(f"{index}\n")
        f.write(
          f"{self._format_time(entry['start_time'])} --> {self._format_time(entry['end_time'])}\n"
        )
        f.write(f"{entry['speaker']}: {entry['message']}\n")
        f.write("\n")
