import rainier_core
import io_tools

if __name__ == '__main__':
    down = io_tools.Downland(None)
    down.begin_thread(10)
    rainier_core.get_all_movie_infos(lambda info: down.thread_downland(info))
    down.stop_thread()
    # rainier_core.get_all_movie_infos(lambda info: down.downland_one_with_progress(info))


