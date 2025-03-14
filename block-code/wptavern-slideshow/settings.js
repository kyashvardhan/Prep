import { ToggleControl, SelectControl } from '@wordpress/components';

// Function to render block settings
export const SlideshowSettings = ({ attributes, setAttributes }) => (
  <>
    <SelectControl
      label="Transition Speed"
      value={attributes.transitionSpeed}
      options={[
        { label: 'Fast', value: '500' },
        { label: 'Medium', value: '1000' },
        { label: 'Slow', value: '2000' }
      ]}
      onChange={value => setAttributes({ transitionSpeed: value })}
    />
    <ToggleControl
      label="Show Navigation Dots"
      checked={attributes.showDots}
      onChange={value => setAttributes({ showDots: value })}
    />
    <ToggleControl
      label="Loop Slideshow"
      checked={attributes.loop}
      onChange={value => setAttributes({ loop: value })}
    />
  </>
);
