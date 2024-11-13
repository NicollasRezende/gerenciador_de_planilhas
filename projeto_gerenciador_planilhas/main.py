import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk
from controllers import sheet_controller, log_controller, export_controller
from config import WINDOW_TITLE

# Configuração inicial da interface
class App(ThemedTk):
    def __init__(self):
        super().__init__(theme="equilux")  # Aplicando o tema dark
        self.title(WINDOW_TITLE)
        self.geometry("800x600")
        
        # Inicializa os componentes da interface
        self.create_widgets()

    def create_widgets(self):
        # Título principal
        title_label = ttk.Label(self, text="Controle de Inventário", font=("Helvetica", 16))
        title_label.pack(pady=10)

        # Botões principais
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=20)

        btn_view_data = ttk.Button(btn_frame, text="Carregar Dados", command=self.load_data)
        btn_view_data.grid(row=0, column=0, padx=10)
        btn_edit_inventory = ttk.Button(btn_frame, text="Editar Inventário", command=self.edit_inventory)
        btn_edit_inventory.grid(row=0, column=1, padx=10)
        btn_export_data = ttk.Button(btn_frame, text="Exportar Dados", command=self.export_data)
        btn_export_data.grid(row=0, column=2, padx=10)
        btn_view_logs = ttk.Button(btn_frame, text="Visualizar Logs", command=self.view_logs)
        btn_view_logs.grid(row=0, column=3, padx=10)

        # Área de exibição de dados
        self.data_display = ttk.Treeview(self, columns=("Item", "Localização", "Quantidade"), show="headings")
        self.data_display.heading("Item", text="Item")
        self.data_display.heading("Localização", text="Localização")
        self.data_display.heading("Quantidade", text="Quantidade")
        self.data_display.pack(fill=tk.BOTH, expand=True)

    def load_data(self):
        """Carrega e exibe os dados da planilha na interface."""
        try:
            sheet = sheet_controller.get_sheet('1xZE1h-sF9u-uXxeZEsoyix4-42xRb1YRnoi82K9BU8c')
            data = sheet.get_all_records()
            self.data_display.delete(*self.data_display.get_children())
            for row in data:
                self.data_display.insert("", "end", values=(row['Item'], row['Localização'], row['Quantidade']))
        except Exception as e:
            messagebox.showerror("Erro ao carregar dados", str(e))

    def edit_inventory(self):
        """Função para editar o inventário (a ser implementada)."""
        messagebox.showinfo("Em Desenvolvimento", "Funcionalidade de edição ainda não implementada.")

    def export_data(self):
        """Exporta os dados carregados para um arquivo CSV."""
        try:
            data = [self.data_display.item(item)["values"] for item in self.data_display.get_children()]
            export_controller.export_sheet_to_csv(data, "export_inventario")
            messagebox.showinfo("Exportação Concluída", "Dados exportados com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro ao exportar dados", str(e))

    def view_logs(self):
        """Exibe os logs de ações registradas."""
        try:
            logs = log_controller.read_logs()
            log_text = "\n".join([f"{log['timestamp']} - {log['user']} - {log['action']} - {log['details']}" for log in logs])
            log_window = tk.Toplevel(self)
            log_window.title("Logs de Ações")
            text_area = tk.Text(log_window, wrap="word", bg="#2e2e2e", fg="#ffffff")
            text_area.insert("1.0", log_text)
            text_area.pack(fill="both", expand=True)
            text_area.config(state="disabled")
        except Exception as e:
            messagebox.showerror("Erro ao visualizar logs", str(e))

# Inicia a aplicação
if __name__ == "__main__":
    app = App()
    app.mainloop()
