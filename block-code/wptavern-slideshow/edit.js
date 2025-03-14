import { useState, useEffect } from '@wordpress/element';
import { useBlockProps, InspectorControls } from '@wordpress/block-editor';
import { PanelBody, ToggleControl } from '@wordpress/components';
import apiFetch from '@wordpress/api-fetch';
import Slideshow from './Slideshow';

// Function to fetch posts from WPTavern API
const fetchPosts = async () => {
  try {
    const response = await apiFetch({
      url: 'https://wptavern.com/wp-json/wp/v2/posts?per_page=5&_embed=1'
    });
    return response;
  } catch (error) {
    console.error('Error fetching posts:', error);
    return [];
  }
};

export default function Edit({ attributes, setAttributes }) {
  const [posts, setPosts] = useState([]);
  const blockProps = useBlockProps();

  useEffect(() => {
    fetchPosts().then(data => setPosts(data));
  }, []);

  return (
    <div {...blockProps}>
      <InspectorControls>
        <PanelBody title="Settings">
          <ToggleControl
            label="Auto-scroll"
            checked={attributes.autoScroll}
            onChange={value => setAttributes({ autoScroll: value })}
          />
          <ToggleControl
            label="Show Dates"
            checked={attributes.showDate}
            onChange={value => setAttributes({ showDate: value })}
          />
        </PanelBody>
      </InspectorControls>
      {posts.length > 0 && (
        <Slideshow posts={posts} attributes={attributes} isEditing={true} />
      )}
    </div>
  );
}
