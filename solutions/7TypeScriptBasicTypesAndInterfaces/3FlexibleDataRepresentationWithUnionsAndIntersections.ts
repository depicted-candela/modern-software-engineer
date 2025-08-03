type Media = { id: number; sourceUrl: string; }
type Video = Media & { duration: number; }
type Image = Media & { width: number; height: number; }
type PromotableContent = Video | Image;
type PromotedPost = PromotableContent & { sponsor: string; campaignId: string };

const promotedVideo = {
    id: 1,
    sourceUrl: "https://example.com/video.mp4",
    duration: 120,
    sponsor: "TechCorp",
    campaignId: "TC-001"
};

const promotedImage = {
    id: 2,
    sourceUrl: "https://example.com/image.jpg",
    width: 1920,
    height: 1080,
    sponsor: "AdCo",
    campaignId: "AC-002"
};

const promotedVideoT: PromotedPost = promotedVideo;
const promotedImageT: PromotedPost = promotedImage;

console.log(promotedVideoT);
console.log(promotedImageT);