import { useState, useEffect } from '@wordpress/element';
import useKeyboardNavigation from './useKeyboardNavigation';

// Function to handle navigation
const handleNavigation = (direction, setCurrentSlide, postsLength) => {
  setCurrentSlide(prev => Math.max(0, Math.min(postsLength - 1, prev + direction)));
};

export default function Slideshow({ posts, attributes, isEditing }) {
  const [currentSlide, setCurrentSlide] = useState(0);
  const { onPrev, onNext } = useKeyboardNavigation(
    () => handleNavigation(-1, setCurrentSlide, posts.length),
    () => handleNavigation(1, setCurrentSlide, posts.length)
  );

  useEffect(() => {
    if (attributes.autoScroll && !isEditing) {
      const interval = setInterval(() => {
        setCurrentSlide(prev => (prev + 1) % posts.length);
      }, 5000);
      return () => clearInterval(interval);
    }
  }, [attributes.autoScroll, posts.length, isEditing]);

  return (
    <div className="wp-tavern-slideshow">
      {posts.map((post, index) => (
        <div 
          key={post.id}
          className={`slide ${index === currentSlide ? 'active' : ''}`}
        >
          <a href={post.link} target="_blank" rel="noopener noreferrer">
            <img 
              src={post.featured_media?.source_url || ''} 
              alt={post.title.rendered}
            />
            <h3 dangerouslySetInnerHTML={{ __html: post.title.rendered }} />
          </a>
          {attributes.showDate && (
            <time>{new Date(post.date).toLocaleDateString()}</time>
          )}
        </div>
      ))}
      <div className="controls">
        <button onClick={onPrev}>Previous</button>
        <button onClick={onNext}>Next</button>
      </div>
    </div>
  );
}
