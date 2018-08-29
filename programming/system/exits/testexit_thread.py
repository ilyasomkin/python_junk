import _thread


exit_count = 0


def child():
    global exit_count
    exit_count += 1
    thread_id = _thread.get_ident()
    print('Hello from child', thread_id, exit_count)
    _thread.exit()


def parent():
    while True:
        _thread.start_new_thread(child, ())
        if input() == 'q':
            break


if __name__ == '__main__':
    parent()
