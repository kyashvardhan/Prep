import { registerBlockType } from '@wordpress/blocks';
import Edit from './edit';
import './style.scss';

// Register the block type
registerBlockType('wptavern/slideshow', {
  title: 'WPTavern Slideshow',
  icon: 'images-alt2',
  category: 'widgets',
  attributes: {
    autoScroll: {
      type: 'boolean',
      default: true
    },
    showDate: {
      type: 'boolean',
      default: true
    }
  },
  edit: Edit,
  save: () => null // Dynamic block
});
