namespace AlarmAppWinForms
{
    partial class Form1
    {
        private System.ComponentModel.IContainer components = null;
        private System.Windows.Forms.TextBox txtTime;
        private System.Windows.Forms.Button btnStart;

        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null)) components.Dispose();
            base.Dispose(disposing);
        }

        private void InitializeComponent()
        {
            this.txtTime = new System.Windows.Forms.TextBox();
            this.btnStart = new System.Windows.Forms.Button();
            this.SuspendLayout();

            // txtTime
            this.txtTime.Font = new System.Drawing.Font("Segoe UI", 12F);
            this.txtTime.Location = new System.Drawing.Point(30, 30);
            this.txtTime.Name = "txtTime";
            this.txtTime.PlaceholderText = "HH:MM:SS";
            this.txtTime.Size = new System.Drawing.Size(150, 29);
            this.txtTime.TabIndex = 0;

            // btnStart
            this.btnStart.Font = new System.Drawing.Font("Segoe UI", 12F);
            this.btnStart.Location = new System.Drawing.Point(200, 30);
            this.btnStart.Name = "btnStart";
            this.btnStart.Size = new System.Drawing.Size(100, 30);
            this.btnStart.TabIndex = 1;
            this.btnStart.Text = "Start Alarm";
            this.btnStart.UseVisualStyleBackColor = true;
            this.btnStart.Click += new System.EventHandler(this.btnStart_Click);

            // Form1
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(350, 100);
            this.Controls.Add(this.txtTime);
            this.Controls.Add(this.btnStart);
            this.Name = "Form1";
            this.Text = "Alarm App";
            this.ResumeLayout(false);
            this.PerformLayout();
        }
    }
}
