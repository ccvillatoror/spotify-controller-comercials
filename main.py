import schedule
import time
import spotify_controller as sc
import sound_files_manager as sm

def job():
    sc.pause_spotify()
    sm.play_comercial(sm.choose_random_file())
    sc.resume_spotify()

def main():
    schedule.every(30).minutes.until("21:00").do(job)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()
