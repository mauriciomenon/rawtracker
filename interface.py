import datetime
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from messages import UIMessages
from datetimepicker import DateTimePicker

msg = UIMessages("es")
EXIT_HOUR = 17
EXIT_MINUTE = 0


def today():
    now = datetime.datetime.now()
    return now.replace(hour=EXIT_HOUR, minute=EXIT_MINUTE)

def thisfriday():
    now = datetime.datetime.now()
    (year, week, day) = now.isocalendar()
    return datetime.datetime.fromisocalendar(
            year, week, 5).replace(hour=EXIT_HOUR, minute=EXIT_MINUTE)

def nextweek():
    now = datetime.datetime.now()
    (year, week, day) = now.isocalendar()
    return datetime.datetime.fromisocalendar(year, week+1, day).replace(
        hour=EXIT_HOUR, minute=EXIT_MINUTE)

def nextfriday():
    now = datetime.datetime.now()
    (year, week, day) = now.isocalendar()
    return datetime.datetime.fromisocalendar(
        year, week+1, 5).replace(hour=EXIT_HOUR, minute=EXIT_MINUTE)

class FrameNewTask(tk.Frame):

    def __init__(self, parent, statuses):
        super().__init__(parent)
        self.statuses = statuses
        self.populate()

    def populate(self):
        # Root Grid configuration
        self.grid_columnconfigure(1, weight=1)
        # Task
        self.task_frame = ttk.Labelframe(self, text=msg["task"])
        self.task_frame.grid_columnconfigure(0, weight=1)
        self.task_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))
        self.task_entry = tk.Entry(self.task_frame)
        self.task_entry.grid(row=0, column=0, sticky=(tk.W, tk.E))
        # Planning
        self.planning_frame = ttk.Labelframe(self, text=msg["planning"])
        self.planning_frame.grid_columnconfigure(1, weight=1)
        self.planning_frame.grid(row=1, column=0, sticky=(tk.W, tk.E))
        # Due date
        self.due_frame = ttk.Labelframe(self.planning_frame, text=msg["duedate"])
        self.due_frame.grid_columnconfigure(0, weight=1)
        self.due_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.due_entry = tk.Entry(self.due_frame)
        self.due_entry.grid(row=0, column=0, sticky=(tk.W, tk.E))
        self.due_button = tk.Button(self.due_frame, text=msg["choose"], command=self.pick_due)
        self.due_button.grid(row=0, column=1, sticky=(tk.W, tk.E))
        self.due_context = tk.Menu(self.due_entry, tearoff=False)
        self.due_options = {
            "thisfriday": {"params": {"command": self.set_thisfriday}},
            "nextweek": {"params": {"command": self.set_nextweek}},
            "nextfriday": {"params": {"command": self.set_nextfriday}},
            "Separator": None,
            "customdate": {"params": {"command": self.donothing}},
        }
        self.create_context(self.due_context, self.due_options)
        self.due_entry.bind('<Button-3>', self.context_handler)
        # Status
        self.status_frame = ttk.Labelframe(self.planning_frame, text=msg["status"])
        self.status_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))
        self.status_radio = []
        self.status_var = tk.IntVar()
        for cont, status in enumerate(self.statuses):
            self.status_radio.append(
                tk.Radiobutton(self.status_frame, text=msg[status],
                    variable=self.status_var, value=cont, command=self.toggle_date))
            self.status_radio[cont].grid(row=cont, column=0, sticky=tk.W)
        # Parents
        self.parent_frame = ttk.Labelframe(self, text=msg["parent"])
        self.parent_frame.grid_columnconfigure(0, weight=1)
        self.parent_frame.grid(row=3, column=0, sticky=(tk.W, tk.E))
        self.parent_entry = tk.Label(self.parent_frame, text=" --", anchor=tk.W)
        self.parent_entry.grid(row=0, column=0, sticky=(tk.W, tk.E))
        self.parent_button = tk.Button(self.parent_frame, text=msg["choose"])
        self.parent_button.grid(row=0, column=1, sticky=(tk.W, tk.E))
        # Children
        self.children_frame = ttk.Labelframe(self, text=msg["children"])
        self.children_frame.grid_columnconfigure(0, weight=1)
        self.children_frame.grid(row=4, column=0, sticky=(tk.W, tk.E))
        self.children_entry = tk.Label(self.children_frame, text=" --", anchor=tk.W)
        self.children_entry.grid(row=0, column=0, sticky=(tk.W, tk.E))
        self.children_button = tk.Button(self.children_frame, text=msg["choose"])
        self.children_button.grid(row=0, column=1, sticky=(tk.W, tk.E))
        # Input documents
        self.idoc_frame = ttk.Labelframe(self, text=msg["inputdoc"])
        self.idoc_frame.grid_columnconfigure(0, weight=1)
        self.idoc_frame.grid(row=5, column=0, sticky=(tk.W, tk.E))
        self.idoc_entry = tk.Label(self.idoc_frame, text=" --", anchor=tk.W)
        self.idoc_entry.grid(row=0, column=0, sticky=(tk.W, tk.E))
        self.idoc_button = tk.Button(self.idoc_frame, text=msg["choose"])
        self.idoc_button.grid(row=0, column=1, sticky=(tk.W, tk.E))
        # Output documents
        self.odoc_frame = ttk.Labelframe(self, text=msg["outputdoc"])
        self.odoc_frame.grid_columnconfigure(0, weight=1)
        self.odoc_frame.grid(row=6, column=0, sticky=(tk.W, tk.E))
        self.odoc_entry = tk.Label(self.odoc_frame, text=" --", anchor=tk.W)
        self.odoc_entry.grid(row=0, column=0, sticky=(tk.W, tk.E))
        self.odoc_button = tk.Button(self.odoc_frame, text=msg["choose"])
        self.odoc_button.grid(row=0, column=1, sticky=(tk.W, tk.E))
        # Additional info
        self.info_frame = ttk.Labelframe(self, text=msg["info"])
        self.info_frame.grid_columnconfigure(0, weight=1)
        self.info_frame.grid(row=7, column=0, sticky=(tk.W, tk.E))
        self.info_entry = ScrolledText(self.info_frame, height=5)
        self.info_entry.grid(row=0, column=0, sticky=(tk.W, tk.E))
        self.info_state = tk.IntVar()
        self.info_button = tk.Checkbutton(
            self.info_frame, command=self.toggle_info, variable=self.info_state)
        self.info_button.grid(row=0, column=1, sticky=tk.N)
        self.toggle_info(0)

    def toggle_date(self):
        if self.status_var.get() != 0:
            self.due_entry.delete(0, tk.END)
            self.due_entry.configure(state=tk.DISABLED)
            self.due_button.configure(state=tk.DISABLED)
        else:
            self.due_entry.configure(state=tk.NORMAL)
            self.due_button.configure(state=tk.NORMAL)

    def toggle_info(self, value = None):
        W_STATE = {0: "disable", 1: "normal"}
        W_COLOR = {0: "SystemButtonFace", 1: "SystemWindow"}
        if value is None:
            value = self.info_state.get()
        self.info_entry.config(state=W_STATE[value])
        self.info_entry.config(background=W_COLOR[value])

    def context_handler(self, event):
        if self.status_var.get() == 0:
            self.due_context.tk_popup(event.x_root, event.y_root)

    def create_context(self, parent, options):
        if options is None:
            return
        for option in options:
            if option == "Separator":
                parent.add_separator()
                continue
            parent.add_command(
                label = msg[option],
                **options[option]["params"]
            )

    def set_fixed_due(self, function):
        fixed = {
            "thisfriday": thisfriday,
            "nextfriday": nextfriday,
            "nextweek": nextweek
        }
        self.due_entry.delete(0, tk.END)
        self.due_entry.insert(tk.END, fixed[function]().isoformat(" "))

    def set_thisfriday(self):
        self.set_fixed_due("thisfriday")

    def set_nextfriday(self):
        self.set_fixed_due("nextfriday")

    def set_nextweek(self):
        self.set_fixed_due("nextweek")

    def pick_due(self):
        DateTimePicker(self)

    def donothing(self, *args):
        pass
        

if __name__ == "__main__":
    root = tk.Tk()
    root.title(msg["apptitle"])
    frame = FrameNewTask(root, ["pending", "done", "cancelled"])
    frame.pack(fill=tk.BOTH, expand=True)
    #frame.pick_due()
    root.mainloop()
    
