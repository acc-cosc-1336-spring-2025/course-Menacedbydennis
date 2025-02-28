def get_hour(epoch_seconds):
    total_hours = epoch_seconds // 3600


    return total_hours % 24



def get_minutes (epoch_seconds):
    total_minutes = epoch_seconds // 60

    return total_minutes % 60


def get_seconds(epoch_seconds):
    remaining_seconds = epoch_seconds % 3600

    total_seconds = remaining_seconds % 60


    return total_seconds