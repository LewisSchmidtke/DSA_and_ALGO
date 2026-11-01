from dataclasses import dataclass

class VideoSharingPlatform:
    def __init__(self):
        self.ids = list(range(0,100000))
        heapq.heapify(self.ids)
        self.available_ids = set(self.ids)

        self.video_data = {}


    def upload(self, video: str) -> int:
        new_id = heapq.heappop(self.ids)
        self.available_ids.remove(new_id)
        new_video = VideoMetadata(
            id=new_id, 
            video_content=video,
            video_length=len(video)
        )
        self.video_data[new_id] = new_video

        return new_id

    def remove(self, videoId: int) -> None:
        if videoId in self.available_ids:
            return
        
        heapq.heappush(self.ids, videoId)
        self.available_ids.add(videoId)
        self.video_data.pop(videoId)
        
    def watch(self, videoId: int, startMinute: int, endMinute: int) -> str:
        if videoId in self.available_ids:
            return "-1"

        self.video_data[videoId].views += 1
        length_border = min(endMinute, self.video_data[videoId].video_length)

        return self.video_data[videoId].video_content[startMinute:length_border + 1]

    def like(self, videoId: int) -> None:
        if videoId in self.available_ids:
            return

        self.video_data[videoId].likes += 1

    def dislike(self, videoId: int) -> None:
        if videoId in self.available_ids:
            return

        self.video_data[videoId].dislikes += 1    

    def getLikesAndDislikes(self, videoId: int) -> List[int]:
        if videoId in self.available_ids:
            return [-1]
        
        return [self.video_data[videoId].likes, self.video_data[videoId].dislikes]

    def getViews(self, videoId: int) -> int:
        if videoId in self.available_ids:
            return -1

        return self.video_data[videoId].views

@dataclass
class VideoMetadata:
    id : int
    video_content : str
    video_length : int
    views : int = 0
    likes : int = 0
    dislikes : int = 0
