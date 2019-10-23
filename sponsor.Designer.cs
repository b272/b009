namespace WindowsFormsApp1
{
    partial class Sponsor
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.panel2 = new System.Windows.Forms.Panel();
            this.label14 = new System.Windows.Forms.Label();
            this.button1 = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.Name1 = new System.Windows.Forms.TextBox();
            this.label6 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.runner = new System.Windows.Forms.ComboBox();
            this.runner1BindingSource = new System.Windows.Forms.BindingSource(this.components);
            this.bdDataSet1 = new WindowsFormsApp1.bdDataSet();
            this.label5 = new System.Windows.Forms.Label();
            this.Name_card = new System.Windows.Forms.TextBox();
            this.label7 = new System.Windows.Forms.Label();
            this.nm_card = new System.Windows.Forms.TextBox();
            this.label8 = new System.Windows.Forms.Label();
            this.card1 = new System.Windows.Forms.TextBox();
            this.card2 = new System.Windows.Forms.TextBox();
            this.label9 = new System.Windows.Forms.Label();
            this.cvc = new System.Windows.Forms.TextBox();
            this.label10 = new System.Windows.Forms.Label();
            this.label11 = new System.Windows.Forms.Label();
            this.label12 = new System.Windows.Forms.Label();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.buy = new System.Windows.Forms.Button();
            this.button5 = new System.Windows.Forms.Button();
            this.runner1TableAdapter = new WindowsFormsApp1.bdDataSetTableAdapters.Runner1TableAdapter();
            this.label15 = new System.Windows.Forms.Label();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.panel2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.runner1BindingSource)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.bdDataSet1)).BeginInit();
            this.SuspendLayout();
            // 
            // panel2
            // 
            this.panel2.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
            this.panel2.Controls.Add(this.label14);
            this.panel2.Controls.Add(this.button1);
            this.panel2.Location = new System.Drawing.Point(1, 0);
            this.panel2.Name = "panel2";
            this.panel2.Size = new System.Drawing.Size(772, 61);
            this.panel2.TabIndex = 4;
            // 
            // label14
            // 
            this.label14.AutoSize = true;
            this.label14.Font = new System.Drawing.Font("MS Reference Sans Serif", 17.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label14.ForeColor = System.Drawing.Color.White;
            this.label14.Location = new System.Drawing.Point(133, 15);
            this.label14.Name = "label14";
            this.label14.Size = new System.Drawing.Size(325, 28);
            this.label14.TabIndex = 6;
            this.label14.Text = "MARATHON SKILLS 2019";
            // 
            // button1
            // 
            this.button1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center;
            this.button1.Font = new System.Drawing.Font("Arial", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.button1.Location = new System.Drawing.Point(12, 12);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(88, 31);
            this.button1.TabIndex = 4;
            this.button1.Text = "Назад";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("MS Reference Sans Serif", 17.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label1.ForeColor = System.Drawing.Color.Gray;
            this.label1.Location = new System.Drawing.Point(284, 92);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(216, 28);
            this.label1.TabIndex = 6;
            this.label1.Text = "Спонсор бегуна";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("MS Reference Sans Serif", 13F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label3.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
            this.label3.Location = new System.Drawing.Point(31, 143);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(714, 69);
            this.label3.TabIndex = 7;
            this.label3.Text = "Пожалуйста выберите бегуна, которого вы хотели бы спонсировать\r\nи сумму, которую " +
    "вы хотели бы спонсировать. Спасибо за вашу \r\nподдержку бегунов и их благотворите" +
    "льных учреждений.\r\n";
            this.label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label4.ForeColor = System.Drawing.SystemColors.AppWorkspace;
            this.label4.Location = new System.Drawing.Point(12, 258);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(253, 24);
            this.label4.TabIndex = 19;
            this.label4.Text = "Информация о спонсоре";
            // 
            // Name1
            // 
            this.Name1.Location = new System.Drawing.Point(194, 317);
            this.Name1.Name = "Name1";
            this.Name1.Size = new System.Drawing.Size(141, 20);
            this.Name1.TabIndex = 26;
            this.Name1.Tag = "Enter you Email adress";
            this.Name1.TextChanged += new System.EventHandler(this.Name_TextChanged);
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Font = new System.Drawing.Font("MS Reference Sans Serif", 13F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label6.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
            this.label6.Location = new System.Drawing.Point(108, 318);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(60, 23);
            this.label6.TabIndex = 25;
            this.label6.Text = "Имя:";
            this.label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.label6.Click += new System.EventHandler(this.label6_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("MS Reference Sans Serif", 13F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label2.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
            this.label2.Location = new System.Drawing.Point(91, 357);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(77, 23);
            this.label2.TabIndex = 25;
            this.label2.Text = "Бегун:";
            this.label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.label2.Click += new System.EventHandler(this.label6_Click);
            // 
            // runner
            // 
            this.runner.DataSource = this.runner1BindingSource;
            this.runner.DisplayMember = "Name";
            this.runner.FormattingEnabled = true;
            this.runner.Location = new System.Drawing.Point(194, 356);
            this.runner.Name = "runner";
            this.runner.Size = new System.Drawing.Size(141, 21);
            this.runner.TabIndex = 27;
            this.runner.ValueMember = "RunnerId";
            // 
            // runner1BindingSource
            // 
            this.runner1BindingSource.DataMember = "Runner1";
            this.runner1BindingSource.DataSource = this.bdDataSet1;
            // 
            // bdDataSet1
            // 
            this.bdDataSet1.DataSetName = "bdDataSet";
            this.bdDataSet1.SchemaSerializationMode = System.Data.SchemaSerializationMode.IncludeSchema;
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Font = new System.Drawing.Font("MS Reference Sans Serif", 13F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label5.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
            this.label5.Location = new System.Drawing.Point(90, 397);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(78, 23);
            this.label5.TabIndex = 25;
            this.label5.Text = "Карта:";
            this.label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.label5.Click += new System.EventHandler(this.label6_Click);
            // 
            // Name_card
            // 
            this.Name_card.Location = new System.Drawing.Point(194, 399);
            this.Name_card.Name = "Name_card";
            this.Name_card.Size = new System.Drawing.Size(141, 20);
            this.Name_card.TabIndex = 26;
            this.Name_card.Tag = "Enter you Email adress";
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Font = new System.Drawing.Font("MS Reference Sans Serif", 13F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label7.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
            this.label7.Location = new System.Drawing.Point(16, 438);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(152, 23);
            this.label7.TabIndex = 25;
            this.label7.Text = "Номер карты:";
            this.label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.label7.Click += new System.EventHandler(this.label6_Click);
            // 
            // nm_card
            // 
            this.nm_card.Location = new System.Drawing.Point(194, 441);
            this.nm_card.Name = "nm_card";
            this.nm_card.Size = new System.Drawing.Size(141, 20);
            this.nm_card.TabIndex = 26;
            this.nm_card.Tag = "Enter you Email adress";
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Font = new System.Drawing.Font("MS Reference Sans Serif", 13F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label8.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
            this.label8.Location = new System.Drawing.Point(-3, 476);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(171, 23);
            this.label8.TabIndex = 25;
            this.label8.Text = "Срок действия:";
            this.label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.label8.Click += new System.EventHandler(this.label6_Click);
            // 
            // card1
            // 
            this.card1.Location = new System.Drawing.Point(194, 480);
            this.card1.Name = "card1";
            this.card1.Size = new System.Drawing.Size(35, 20);
            this.card1.TabIndex = 26;
            this.card1.Tag = "Enter you Email adress";
            // 
            // card2
            // 
            this.card2.Location = new System.Drawing.Point(246, 480);
            this.card2.Name = "card2";
            this.card2.Size = new System.Drawing.Size(56, 20);
            this.card2.TabIndex = 26;
            this.card2.Tag = "Enter you Email adress";
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Font = new System.Drawing.Font("MS Reference Sans Serif", 13F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label9.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
            this.label9.Location = new System.Drawing.Point(108, 517);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(60, 23);
            this.label9.TabIndex = 25;
            this.label9.Text = "CVC:";
            this.label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.label9.Click += new System.EventHandler(this.label6_Click);
            // 
            // cvc
            // 
            this.cvc.Location = new System.Drawing.Point(194, 520);
            this.cvc.Name = "cvc";
            this.cvc.Size = new System.Drawing.Size(57, 20);
            this.cvc.TabIndex = 26;
            this.cvc.Tag = "Enter you Email adress";
            // 
            // label10
            // 
            this.label10.AutoSize = true;
            this.label10.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label10.ForeColor = System.Drawing.SystemColors.AppWorkspace;
            this.label10.Location = new System.Drawing.Point(420, 258);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(231, 24);
            this.label10.TabIndex = 19;
            this.label10.Text = "Благотворительность";
            // 
            // label11
            // 
            this.label11.AutoSize = true;
            this.label11.Font = new System.Drawing.Font("MS Reference Sans Serif", 12.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label11.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
            this.label11.Location = new System.Drawing.Point(463, 302);
            this.label11.Name = "label11";
            this.label11.Size = new System.Drawing.Size(140, 22);
            this.label11.TabIndex = 25;
            this.label11.Text = "Фонд Кошелек";
            this.label11.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.label11.Click += new System.EventHandler(this.label6_Click);
            // 
            // label12
            // 
            this.label12.AutoSize = true;
            this.label12.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label12.ForeColor = System.Drawing.SystemColors.AppWorkspace;
            this.label12.Location = new System.Drawing.Point(420, 353);
            this.label12.Name = "label12";
            this.label12.Size = new System.Drawing.Size(235, 24);
            this.label12.TabIndex = 19;
            this.label12.Text = "Сумма пожертвования";
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(467, 476);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(37, 23);
            this.button2.TabIndex = 28;
            this.button2.Text = "-";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(588, 476);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(37, 23);
            this.button3.TabIndex = 28;
            this.button3.Text = "+";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // buy
            // 
            this.buy.Location = new System.Drawing.Point(424, 513);
            this.buy.Name = "buy";
            this.buy.Size = new System.Drawing.Size(111, 35);
            this.buy.TabIndex = 33;
            this.buy.Text = "Заплатить";
            this.buy.UseVisualStyleBackColor = true;
            this.buy.Click += new System.EventHandler(this.buy_Click);
            // 
            // button5
            // 
            this.button5.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center;
            this.button5.Font = new System.Drawing.Font("Arial", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.button5.Location = new System.Drawing.Point(554, 513);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(111, 35);
            this.button5.TabIndex = 32;
            this.button5.Text = "Отмена";
            this.button5.UseVisualStyleBackColor = true;
            this.button5.Click += new System.EventHandler(this.button5_Click);
            // 
            // runner1TableAdapter
            // 
            this.runner1TableAdapter.ClearBeforeFill = true;
            // 
            // label15
            // 
            this.label15.Font = new System.Drawing.Font("Microsoft Sans Serif", 45F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label15.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(64)))), ((int)(((byte)(0)))));
            this.label15.Location = new System.Drawing.Point(412, 397);
            this.label15.Name = "label15";
            this.label15.Size = new System.Drawing.Size(290, 61);
            this.label15.TabIndex = 29;
            this.label15.Text = "50";
            this.label15.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.label15.Click += new System.EventHandler(this.label13_Click);
            // 
            // textBox1
            // 
            this.textBox1.Location = new System.Drawing.Point(510, 476);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(72, 20);
            this.textBox1.TabIndex = 34;
            this.textBox1.Text = "50";
            this.textBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.textBox1.TextChanged += new System.EventHandler(this.textBox1_TextChanged);
            // 
            // Sponsor
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ButtonHighlight;
            this.ClientSize = new System.Drawing.Size(773, 583);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.buy);
            this.Controls.Add(this.button5);
            this.Controls.Add(this.label15);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.runner);
            this.Controls.Add(this.card2);
            this.Controls.Add(this.cvc);
            this.Controls.Add(this.card1);
            this.Controls.Add(this.nm_card);
            this.Controls.Add(this.label9);
            this.Controls.Add(this.label8);
            this.Controls.Add(this.Name_card);
            this.Controls.Add(this.label7);
            this.Controls.Add(this.Name1);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label11);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.label12);
            this.Controls.Add(this.label10);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.panel2);
            this.Name = "Sponsor";
            this.Text = "sponsor";
            this.Load += new System.EventHandler(this.Sponsor_Load);
            this.panel2.ResumeLayout(false);
            this.panel2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.runner1BindingSource)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.bdDataSet1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Panel panel2;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.TextBox Name1;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.ComboBox runner;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.TextBox Name_card;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.TextBox nm_card;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.TextBox card1;
        private System.Windows.Forms.TextBox card2;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.TextBox cvc;
        private System.Windows.Forms.Label label10;
        private System.Windows.Forms.Label label11;
        private System.Windows.Forms.Label label12;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Button buy;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.Label label14;
        private bdDataSet bdDataSet1;
        private System.Windows.Forms.BindingSource runner1BindingSource;
        private bdDataSetTableAdapters.Runner1TableAdapter runner1TableAdapter;
        private System.Windows.Forms.Label label15;
        private System.Windows.Forms.TextBox textBox1;
    }
}