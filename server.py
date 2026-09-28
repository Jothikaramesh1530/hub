from http.server import SimpleHTTPRequestHandler, HTTPServer
import platform
import os

# --------------------------------------------------------
# STEP 3: CONFIGURE YOUR DETAILS HERE BEFORE RUNNING
STUDENT_NAME = "Jothika"
REGISTER_NUMBER = "26016924"
# --------------------------------------------------------

class SpecsHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            
            # HTML response containing student info and system specs
            html_content = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Laptop Specifications - {STUDENT_NAME}</title>
                <style>
                    body {{ font-family: Arial, sans-serif; background-color: #f4f4f9; margin: 40px; color: #333; }}
                    .container {{ max-width: 650px; background: white; padding: 25px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); margin: auto; }}
                    h1 {{ color: #007BFF; border-bottom: 2px solid #007BFF; padding-bottom: 10px; margin-bottom: 20px; }}
                    h2 {{ color: #28a745; margin-top: 0; }}
                    .student-info {{ background-color: #e9ecef; padding: 15px; border-radius: 5px; margin-bottom: 20px; border-left: 5px solid #28a745; }}
                    ul {{ list-style-type: none; padding: 0; }}
                    li {{ padding: 10px 0; border-bottom: 1px solid #eee; font-size: 16px; }}
                    strong {{ color: #555; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Assignment Submission</h1>
                    
                    <!-- Student Details -->
                    <div class="student-info">
                        <h2>Student Details</h2>
                        <p><strong>Name:</strong> {STUDENT_NAME}</p>
                        <p><strong>Register Number:</strong> {REGISTER_NUMBER}</p>
                    </div>

                    <!-- Device Specifications -->
                    <h2>Device Specifications</h2>
                    <ul>
                        <li><strong>Computer Name:</strong> {platform.node()}</li>
                        <li><strong>Operating System:</strong> {platform.system()} {platform.release()}</li>
                        <li><strong>Architecture:</strong> {platform.machine()}</li>
                        <li><strong>Processor:</strong> {platform.processor()}</li>
                        <li><strong>CPU Cores:</strong> {os.cpu_count()}</li>
                    </ul>
                </div>
            </body>
            </html>
            """
            self.wfile.write(html_content.encode('utf-8'))
        else:
            super().do_GET()

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SpecsHandler)
    print(f"🚀 Server running locally at http://127.0.0.1:{port}/")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped.")
>
                    </        httpd.server_close()

if __name__ == '__main__':
    run_server(port=8000)
