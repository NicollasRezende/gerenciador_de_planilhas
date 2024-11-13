import tkinter as tk
from tkinter import messagebox
from services.google_sheets_service import open_sheet, read_data
from services.auth_service import has_permission, is_admin
from config import GOOGLE_SHEETS_URL, ADMIN_USERS, DASHBOARD_REFRESH_INTERVAL

class DashboardView:
    def __init__(self, root, user_email):
        self.root = root
        self.user_email = user_email
        self.root.title("Painel de Controle - Gerenciador de Inventário")
        self.root.geometry("800x600")
        
        # Configurar interface
        self.create_widgets()
        self.update_dashboard()
        
    def create_widgets(self):
        """Cria os widgets do painel de controle."""
        self.inventory_label = tk.Label(self.root, text="Inventário", font=("Arial", 16))
        self.inventory_label.pack(pady=10)

        self.inventory_list = tk.Listbox(self.root, width=100, height=20)
        self.inventory_list.pack(pady=5)

        # Botão para exportar dados
        if has_permission("admin" if is_admin(self.user_email) else "user", "export_data"):
            self.export_button = tk.Button(self.root, text="Exportar Dados", command=self.export_data)
            self.export_button.pack(pady=10)

        # Botão para visualizar logs
        if has_permission("admin" if is_admin(self.user_email) else "user", "view_logs"):
            self.logs_button = tk.Button(self.root, text="Visualizar Logs", command=self.view_logs)
            self.logs_button.pack(pady=5)

    def update_dashboard(self):
        """Atualiza o painel com dados do inventário."""
        # Conecta com o Google Sheets para ler os dados
        try:
            sheet_id = GOOGLE_SHEETS_URL.split('/d/')[1].split('/')[0]
            sheet = open_sheet(sheet_id)
            data = read_data(sheet, "A1:Z100")  # Ajuste o intervalo conforme necessário

            self.inventory_list.delete(0, tk.END)
            for row in data:
                self.inventory_list.insert(tk.END, " | ".join(row))

            # Atualiza a cada X segundos
            self.root.after(DASHBOARD_REFRESH_INTERVAL * 1000, self.update_dashboard)

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar o inventário: {e}")

    def export_data(self):
        """Exporta os dados do inventário para um arquivo."""
        # Lógica de exportação
        messagebox.showinfo("Exportação", "Dados exportados com sucesso!")

    def view_logs(self):
        """Abre uma nova janela para exibir os logs."""
        # Lógica para exibir logs
        messagebox.showinfo("Logs", "Exibindo logs do sistema.")

# Código principal para iniciar o painel
if __name__ == "__main__":
    root = tk.Tk()
    user_email = "user@example.com"  # Este email deve vir do sistema de autenticação
    dashboard = DashboardView(root, user_email)
    root.mainloop()
