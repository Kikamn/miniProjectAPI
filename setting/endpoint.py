# HOST
import os

host_gorest = "https://gorest.co.in/public/v2" #link ngambil dari api
host_qase_io = "https://api.qase.io/v1" # ambil link dari https://developers.qase.io/reference/get-results

# ENDPOINT
api_user = host_gorest + "/users"
api_user_wrong = host_gorest + "/user"
api_result = host_qase_io + "/result/"  #akan jadi https://api.qase.io/v1/result/

# CONFIQ = TOKEN YANG DIAMBIL DARI QASE.IO

TOKEN_QASE_IO = os.environ.get('QASE_IO_TOKEN') #setelah di set di github
PROJECT_QASE_IO = "DEMO" # ambil dari https://app.qase.io/project/DEMO
TEST_RUNING_QASE_IO = "1" # ambil dari https://app.qase.io/run/DEMO/dashboard/1

# ======================================== SLACK ========================================

WEBHOOK = os.environ.get('WEBHOOK_SLACK') #setelah di set di github

# ======================================== NETLIFY ========================================
URL_NETLIFY = os.environ.get('URL_NETLIFY')