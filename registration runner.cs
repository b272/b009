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
    public partial class Registration_runner : Form
    {
        public Registration_runner()
        {
            InitializeComponent();
        }

        private void label9_Click(object sender, EventArgs e)
        {

        }

        private void label6_Click(object sender, EventArgs e)
        {

        }

        private void email_Enter(object sender, EventArgs e)
        {
            TextBox t = (TextBox) sender;
            if (t.Tag == null)
            {
                t.Tag = t.Text;
                t.Text = "";
            }
            else
                if ((string)t.Tag == t.Text) t.Text = "";
            t.ForeColor = Color.Black;
        }

        private void email_Leave(object sender, EventArgs e)
        {
            TextBox t = (TextBox)sender;
            if(t.Text == "")
            {
                t.Text = (string)t.Tag;
                t.ForeColor = Color.Gray;
              
            }
        }

        private void email_TextChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            Home home = new Home();
            home.Show();
            this.Hide();
        }

        private void button3_Click(object sender, EventArgs e)
        {

        }
    }
}
