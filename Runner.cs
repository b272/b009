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
    public partial class Runner : Form
    {
        public Runner()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Home home = new Home();
            home.Show();
            this.Hide();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Login_User new_User = new Login_User();
            new_User.Show();
            this.Hide();                                                                                                                                                                                                                                            
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Registration_runner registration_runner = new Registration_runner();
            registration_runner.Show();
            this.Hide();
        }

        private void button5_Click(object sender, EventArgs e)
        {

        }
    }
}
