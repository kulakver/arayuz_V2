import tkinter
import tkinter.messagebox
import customtkinter
from tkcalendar import Calendar
from PIL import Image,ImageTk

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(6, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Test", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.test_label = customtkinter.CTkLabel(self.sidebar_frame, text="Toplantı Özetleri", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.test_label.grid(row=1, column=0, padx=20, pady=(20, 10))
        #self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        #self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        #self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        #self.sidebar_button_2.grid(row=1, column=0, padx=20, pady=10)
        self.textbox = customtkinter.CTkTextbox(self.sidebar_frame, width=250)
        self.textbox.grid(row=2, column=0, padx=(20, 0), pady=(10, 0), sticky="nsew")
        self.sidebar_button_create_avatar = customtkinter.CTkButton(self.sidebar_frame, text="Create Avatar", command=self.sidebar_button_event)
        self.sidebar_button_create_avatar.grid(row=3, column=0, pady=5)
        self.sidebar_button_edit_avatar = customtkinter.CTkButton(self.sidebar_frame, text="Edit Avatar", command=self.sidebar_button_event)
        self.sidebar_button_edit_avatar.grid(row=4,column=0, pady=10)
        self.sidebar_button_about = customtkinter.CTkButton(self.sidebar_frame, text="About", command=self.sidebar_button_event)
        self.sidebar_button_about.grid(row=5, column=0)
        
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame,text="")
        self.appearance_mode_label.grid(row=6, column=0, padx=20, pady=(10, 0))
        self.calendar = Calendar(self.sidebar_frame)
        self.calendar.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=8, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=9, column=0, padx=20, pady=(10, 10))

        # create main entry and button
        
        #self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        #self.picture1 = customtkinter.CTkImage(self.entry,Image.open(r"C:\Users\MonsterPC\Desktop\cv\1616751276754.jpg"))
        #self.photo_label = Label(image=ImageTk.PhotoImage(Image.fromarray(data)))
        #img = ImageTk.PhotoImage(Image.open(r"C:\Users\MonsterPC\Desktop\cv\1616751276754.jpg"))
        self.main_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.main_frame.grid(row=0, column=1, rowspan=5,columnspan=3, sticky="nsew")
        self.main_frame.grid_rowconfigure(5)
        self.main_frame.grid_columnconfigure(3)
        self.main_frame_label = customtkinter.CTkLabel(self.main_frame,text="")
        self.main_frame_label.grid(row=1, column=0, padx=20, pady=(10, 0))
        self.main_frame_label2= customtkinter.CTkLabel(self.main_frame,text="")
        self.main_frame_label2.grid(row=2, column=0, padx=20, pady=(10, 0))
        img = customtkinter.CTkImage(light_image=Image.open(r"C:\Users\MonsterPC\Desktop\cv\1616751276754.jpg"), size=(100, 100))
        self.picture_label=customtkinter.CTkLabel(self.main_frame,image=img,text="")
        self.picture_label.grid(row=3, column=1,padx=20, pady=(10, 10))
        self.picture_label2=customtkinter.CTkLabel(self.main_frame,image=img,text="")
        self.picture_label2.grid(row=3, column=2,padx=20, pady=(10, 10))
        self.picture_label3=customtkinter.CTkLabel(self.main_frame,image=img,text="")
        self.picture_label3.grid(row=3, column=3,padx=20, pady=(10, 10))
        self.main_frame_label3 = customtkinter.CTkLabel(self.main_frame,text="")
        self.main_frame_label3.grid(row=4, column=0, padx=20, pady=(10, 0))
        self.main_frame_button = customtkinter.CTkButton(self.main_frame, text="Dinle")
        self.main_frame_button.grid(row=5, column=2)
       
       
        '''
        self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")
        '''
        # create textbox
        #self.textbox = customtkinter.CTkTextbox(self, width=250)
        #self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        '''
        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("CTkTabview")
        self.tabview.add("Tab 2")
        self.tabview.add("Tab 3")
        self.tabview.tab("CTkTabview").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Tab 2").grid_columnconfigure(0, weight=1)
        
        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("CTkTabview"), dynamic_resizing=False,
                                                        values=["Value 1", "Value 2", "Value Long Long Long"])
        self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.combobox_1 = customtkinter.CTkComboBox(self.tabview.tab("CTkTabview"),
                                                    values=["Value 1", "Value 2", "Value Long....."])
        self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("CTkTabview"), text="Open CTkInputDialog",
                                                           command=self.open_input_dialog_event)
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Tab 2"), text="CTkLabel on Tab 2")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)
        '''
        
        '''
        # create radiobutton frame
        self.radiobutton_frame = customtkinter.CTkFrame(self)
        self.radiobutton_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="CTkRadioButton Group:")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=0)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=1)
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=2)
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")
        '''
        '''
        # create checkbox and switch frame
        self.checkbox_slider_frame = customtkinter.CTkFrame(self)
        self.checkbox_slider_frame.grid(row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.checkbox_1 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        self.checkbox_1.grid(row=1, column=0, pady=(20, 10), padx=20, sticky="n")
        self.checkbox_2 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        self.checkbox_2.grid(row=2, column=0, pady=10, padx=20, sticky="n")
        self.switch_1 = customtkinter.CTkSwitch(master=self.checkbox_slider_frame, command=lambda: print("switch 1 toggle"))
        self.switch_1.grid(row=3, column=0, pady=10, padx=20, sticky="n")
        self.switch_2 = customtkinter.CTkSwitch(master=self.checkbox_slider_frame)
        self.switch_2.grid(row=4, column=0, pady=(10, 20), padx=20, sticky="n")
        '''
        '''
        # create slider and progressbar frame
        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=1, column=1, columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
        self.seg_button_1 = customtkinter.CTkSegmentedButton(self.slider_progressbar_frame)
        self.seg_button_1.grid(row=0, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        self.progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.progressbar_2 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        self.progressbar_2.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.slider_1 = customtkinter.CTkSlider(self.slider_progressbar_frame, from_=0, to=1, number_of_steps=4)
        self.slider_1.grid(row=3, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.slider_2 = customtkinter.CTkSlider(self.slider_progressbar_frame, orientation="vertical")
        self.slider_2.grid(row=0, column=1, rowspan=5, padx=(10, 10), pady=(10, 10), sticky="ns")
        self.progressbar_3 = customtkinter.CTkProgressBar(self.slider_progressbar_frame, orientation="horizontal")
        self.progressbar_3.grid(row=0, column=2, rowspan=5, padx=(10, 20), pady=(10, 10), sticky="ns")
        '''
        '''
        # set default values
        #self.sidebar_button_3.configure(state="disabled", text="Disabled CTkButton")
        self.checkbox_2.configure(state="disabled")
        self.switch_2.configure(state="disabled")
        self.checkbox_1.select()
        self.switch_1.select()
        self.radio_button_3.configure(state="disabled")
        self.appearance_mode_optionemenu.set("Dark")
#       self.scaling_optionemenu.set("100%")
        self.optionmenu_1.set("CTkOptionmenu")
        self.combobox_1.set("CTkComboBox")
        self.slider_1.configure(command=self.progressbar_2.set)
        self.slider_2.configure(command=self.progressbar_3.set)
        self.progressbar_1.configure(mode="indeterminnate")
        self.progressbar_1.start()
        '''
        self.textbox.insert("0.0", "CTkTextbox\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)
        '''
        self.seg_button_1.configure(values=["CTkSegmentedButton", "Value 2", "Value 3"])
        self.seg_button_1.set("Value 2")

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
    '''
    def sidebar_button_event(self):
        print("sidebar_button click")
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
    

    
if __name__ == "__main__":
    app = App()
    app.mainloop()
