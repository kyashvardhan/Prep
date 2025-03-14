import { apiFetch } from '@wordpress/api-fetch';

// Function to fetch posts from WPTavern API
export const fetchWPTavernPosts = async (perPage = 5) => {
  try {
    const response = await apiFetch({
      url: `https://wptavern.com/wp-json/wp/v2/posts?per_page=${perPage}&_embed=1`
    });
    return response;
  } catch (error) {
    console.error('API Error:', error);
    return [];
  }
};
