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
    public partial class Home : Form
    {
        public Home()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged_1(object sender, EventArgs e)
        {

        }

        private void textBox6_TextChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            /*  Form index = new index();
              Runner frm = new Runner();
              this.Hide();
              frm.ShowDialog();
              this.Show();
              index.Visible = false;*/

            Runner runner = new Runner();
            runner.Show();
            this.Hide();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            Login_User new_user = new Login_User();
            new_user.Show();
            this.Hide();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            string data_text = DateTime.Now.ToLongDateString();
            richTextBox1.Text = data_text ;
        }

        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {
            string data_text = DateTime.Now.ToLongDateString();
            richTextBox1.Text = data_text;
        }

        private void richTextBox2_TextChanged(object sender, EventArgs e)
        {
            DateTime time = DateTime.Now;
            time.AddHours(-5);
            richTextBox1.Text = time.ToLongDateString();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Registration_guest registration_guest = new Registration_guest();
            registration_guest.Show();
            this.Hide();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Sponsor sponsor = new Sponsor();
            sponsor.Show();
            this.Hide();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            Find_out_more_information find_out_more_information = new Find_out_more_information();
            find_out_more_information.Show();
            this.Hide();
        }
    }
}
