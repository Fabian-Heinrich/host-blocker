import os

class HostBlocker:

    hostfile_path = os.path.abspath('C:\\Windows\\System32\\drivers\\etc\\hosts')

    def __init__(self, blocklist_path) -> None:
        self.blocklist_path = os.path.abspath(blocklist_path)

    def enable(self):
        hostfile_without_blocker = self.remove_host_blocker_block(self.get_hostfile_buffer())
        hostfile_with_blocker = self.add_host_blocker_block(hostfile_without_blocker)
        
        with open(self.hostfile_path, 'w') as hostfile_handle_write:
            hostfile_handle_write.writelines(hostfile_with_blocker)

    def disable(self):
        hostfile_without_blocker = self.remove_host_blocker_block(self.get_hostfile_buffer())

        with open(self.hostfile_path, 'w') as hostfile_handle_write:
            hostfile_handle_write.writelines(hostfile_without_blocker)


    def get_hostfile_buffer(self):
        with open(self.hostfile_path, 'r') as hostfile_handle_read:
            hostfile_buffer = hostfile_handle_read.readlines()

        return hostfile_buffer

    def get_blocked_hosts(self):
        with open(self.blocklist_path, 'r') as blocklist_handle_read:
            blocklist_buffer = blocklist_handle_read.readlines()
            blocked_hosts = [line.strip() for line in blocklist_buffer]
        return blocked_hosts

    def get_blocked_hosts_line(self):
        return '127.0.0.1 ' + ' '.join(self.get_blocked_hosts()) + '\n'

    def remove_host_blocker_block(self, buffer:list):
        delete_line_start = -1
        delete_line_end = -1
        
        for index, line in enumerate(buffer):
            if line.startswith('## host-blocker-start'):
                delete_line_start = index

            if line.startswith('## host-blocker-end'):
                delete_line_end = index
        
        if delete_line_start != -1 and delete_line_end != -1:
            buffer = buffer[:delete_line_start] + buffer[(delete_line_end+1):]

        return buffer

    def add_host_blocker_block(self, buffer: list):
        return buffer + ['## host-blocker-start\n', self.get_blocked_hosts_line(), '## host-blocker-end\n']