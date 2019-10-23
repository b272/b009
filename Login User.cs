using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    public partial class Login_User : Form
    {
        public Login_User()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Home home = new Home();
            home.Show();
            this.Hide();
        }

        private void label5_Click(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void email_KeyPress(object sender, KeyPressEventArgs e)
        {
            label6.Visible = String.IsNullOrEmpty(email.Text);
        }

        private void label6_Click(object sender, EventArgs e)
        {
            email.Focus();
        }

        private void password_KeyPress(object sender, KeyPressEventArgs e)
        {
            label7.Visible = String.IsNullOrEmpty(password.Text);
        }

        private void label7_Click(object sender, EventArgs e)
        {
            password.Focus();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Home home = new Home();
            home.Show();
            this.Hide();
        }
    }
}
