import os
import tkinter
import datetime
import configparser
import customtkinter

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

wdir = f"{'/'.join(os.path.abspath(__file__).split('/')[:-1])}"

config = configparser.ConfigParser()
config.read("config.ini")

print(f"{wdir}")

description_text = config.get("UI", "ABOUT")
author_text = config.get("UI", "AUTHOR")
version_text = config.get("UI", "VERSION")


def change_appearance_mode_event(new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)


def change_scaling_event(new_scaling: str):
    new_scaling_float = int(new_scaling.replace("%", "")) / 100
    customtkinter.set_widget_scaling(new_scaling_float)


def info_dialog():
    app_second = Info_window()
    app_second.mainloop()


def set_dialog():
    app_second_set = Set_window()
    app_second_set.mainloop()


class Main_window(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title(f'{config.get("UI", "TITLE")} v.{config.get("UI", "VERSION")}')
        self.geometry(f"{600}x{500}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text=config.get("UI", "APPNAME"),
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(70, 10))
        self.logo_label_pre = customtkinter.CTkLabel(self.sidebar_frame, text=config.get("UI", "COPYRIGHT"),
                                                     font=customtkinter.CTkFont(size=10, weight="bold"))
        self.logo_label_pre.grid(row=0, column=0, padx=20, pady=(120, 10))

        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="About",
                                                        command=info_dialog)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=30)

        self.string_input_button = customtkinter.CTkButton(self.sidebar_frame, text="Настройки",
                                                           command=set_dialog)
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(80, 10))

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                       values=["Dark", "Light", "System"],
                                                                       command=change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=3, column=0, padx=10, pady=(20, 0))

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text=f"{version_text}")
        self.appearance_mode_label.grid(row=0, column=0, padx=10, pady=(0, 0))

        self.textbox_info = customtkinter.CTkTextbox(master=self, width=300, font=customtkinter.CTkFont(size=8,
                                                                                                        weight="bold"),
                                                     text_color="grey")

        self.textbox_info.grid(row=1, column=1, padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.textbox_info.insert("0.0",
                                 f'{(config.get("UI", "TITLE").upper())} v.{config.get("UI", "VERSION")} \n\n')
        self.textbox_info.configure(state="disabled")

        self.button_pars = customtkinter.CTkButton(master=self, text="START", command=self.edit_info)
        self.button_pars.grid(row=0, column=1, padx=50, pady=50)

    def enter_log(self, log_text):
        self.textbox_info.configure(state="normal")
        self.textbox_info.insert(tkinter.END, f'[{datetime.datetime.now()}] - {log_text}\n')
        self.textbox_info.see(tkinter.END)
        self.textbox_info.configure(state="disabled")

    def edit_info(self):
        self.textbox_info.configure(state="normal")
        self.textbox_info.insert(tkinter.END, f'[{datetime.datetime.now()}] - Процесс запущен \n')
        self.textbox_info.see(tkinter.END)
        self.textbox_info.configure(state="disabled")

        self.logo_label = customtkinter.CTkLabel(master=self,
                                                 text="ПРОГРАММА ВЫПОЛНЯЕТСЯ. \n НЕ ЗАКРЫВАЙТЕ ПРОГРАММУ "
                                                      "ДО ЗАВЕРШЕНИЯ!",
                                                 font=customtkinter.CTkFont(size=9, weight="bold"), text_color="red")
        self.logo_label.grid(row=0, column=1, padx=20, pady=(90, 10))

        state_code = True

        try:
            # ----------------------------------------------------------------------------------------------------------
            import main

            return_run = main.read_xlsx(config.get("WORK", "WORK_DIR"))

            for return_i in return_run:
                for return_files in return_i:
                    self.enter_log(f"Обрабатывается склад {return_files}")

            # ----------------------------------------------------------------------------------------------------------
        except Exception as er:
            self.textbox_info.configure(state="normal")
            self.textbox_info.insert(tkinter.END, f'[{datetime.datetime.now()}] - {er} \n')
            self.textbox_info.see(tkinter.END)
            self.textbox_info.configure(state="disabled")
            state_code = False

        if state_code:
            finish_status = "Завершено успешно"
            text_col = "green"
        else:
            finish_status = "Завершено c ошибками"
            text_col = "purple"

        self.textbox_info.configure(state="normal")
        self.textbox_info.insert(tkinter.END, f'[{datetime.datetime.now()}] - {finish_status} \n')
        self.textbox_info.see(tkinter.END)
        self.textbox_info.configure(state="disabled")

        self.logo_label = customtkinter.CTkLabel(master=self, text="                                                  "
                                                                   "                                                  ",
                                                 font=customtkinter.CTkFont(size=10, weight="bold"),
                                                 text_color=text_col)
        self.logo_label.grid(row=0, column=1, padx=20, pady=(90, 10))

        self.logo_label = customtkinter.CTkLabel(master=self, text=finish_status,
                                                 font=customtkinter.CTkFont(size=10, weight="bold"),
                                                 text_color=text_col)
        self.logo_label.grid(row=0, column=1, padx=20, pady=(90, 10))


class Info_window(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Информация")
        self.geometry("500x250")
        self.textbox = customtkinter.CTkTextbox(self, width=450, font=customtkinter.CTkFont(size=8, weight="bold"),
                                                text_color="grey")
        self.textbox.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.textbox.insert("0.0",
                            f'{(config.get("UI", "TITLE").upper())} v.{config.get("UI", "VERSION")} \n\n' +
                            f"{description_text}\n\n{author_text}\n\n")
        self.textbox.configure(state="disabled")


class Set_window(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        try:
            self.preset_for = config.get("WORK", "WORK_DIR")
        except:
            self.preset_for = "Введите полный путь"

        self.title("Настройки")
        self.geometry("500x200")

        self.set_info = customtkinter.CTkLabel(self, text=f'{config.get("UI", "INFO_SET")}', anchor="w")
        self.set_info.grid(row=1, column=2, padx=20, pady=(10, 0))

        self.search_dir = customtkinter.CTkLabel(self, text="Путь", anchor="w")
        self.search_dir.grid(row=2, column=0, padx=20, pady=(10, 0))
        self.entry_dir = customtkinter.CTkEntry(self, placeholder_text=f"{self.preset_for}", width=360)
        self.entry_dir.grid(row=2, column=2, columnspan=1, padx=(20, 0), pady=(5, 5), sticky="nsew")

        self.sidebar_button_2 = customtkinter.CTkButton(self, text="Save & Exit", command=self.save_set)
        self.sidebar_button_2.grid(row=8, column=2, columnspan=2, padx=20, pady=30)

    def save_set(self):
        path_dir = self.entry_dir.get()
        try:
            config.add_section("WORK")
        except Exception as ex:
            print(ex)

        config.set("WORK", "WORK_DIR", path_dir)

        with open(f"{wdir}/config.ini", "w") as config_file:
            config.write(config_file)

        Set_window.destroy(self)


def run():
    app = Main_window()
    app.mainloop()


if __name__ == "__main__":
    run()
