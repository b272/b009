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
    public partial class Sponsor : Form
    {
       

        public Sponsor()
        {
            InitializeComponent();
        }

        private void label6_Click(object sender, EventArgs e)
        {

        }

        private void button5_Click(object sender, EventArgs e)
        {
            Home home = new Home();
            home.Show();
            this.Show();

        }

        private void button1_Click(object sender, EventArgs e)
        {
            Home home = new Home();
            home.Show();
            this.Show();
        }

        private void Sponsor_Load(object sender, EventArgs e)
        {
            // TODO: данная строка кода позволяет загрузить данные в таблицу "bdDataSet1.Runner1". При необходимости она может быть перемещена или удалена.
            this.runner1TableAdapter.Fill(this.bdDataSet1.Runner1);
            // TODO: данная строка кода позволяет загрузить данные в таблицу "bdDataSet.User". При необходимости она может быть перемещена или удалена.
            // TODO: данная строка кода позволяет загрузить данные в таблицу "bdDataSet.Runner". При необходимости она может быть перемещена или удалена.
            // TODO: данная строка кода позволяет загрузить данные в таблицу "bdDataSet.Marathon". При необходимости она может быть перемещена или удалена.

        }

        private void Name_TextChanged(object sender, EventArgs e)
        {

             
        }

        private void buy_Click(object sender, EventArgs e)
        {
            if (Name1.Text == "")
            {
                MessageBox.Show("Вы не ввели Имя");
            }
            if (Name_card.Text == "")
            {
                MessageBox.Show("Вы не ввели карту");
            }
            if (nm_card.Text == "")
            {
                MessageBox.Show("Вы не ввели номер карты");
            }
            if (card1.Text == "" || card2.Text == "")
            {
                MessageBox.Show("Вы не ввели срок действия карты");
            }
            if (cvc.Text == "")
            {
                MessageBox.Show("Вы не ввели CVC");
            }


        }

        private void label13_Click(object sender, EventArgs e)
        {
            string a = textBox1.Text;
            int x = int.Parse(a);
            x = x + 10;
            textBox1.Text = x.ToString();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            label15.Text = textBox1.Text;
            string p = textBox1.Text;
            int n = int.Parse(p);
            if (n < 10)
            {
                n = 10;
            }
            textBox1.Text = n.ToString();

        }

        private void button3_Click(object sender, EventArgs e)
        {
            string a = textBox1.Text;
            int x = int.Parse(a);
            x = x + 10;
            textBox1.Text = x.ToString();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string a = textBox1.Text;
            int x = int.Parse(a);
            x = x - 10;
            textBox1.Text = x.ToString();
        }
    }
}
