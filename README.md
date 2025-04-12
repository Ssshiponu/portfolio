# Portfolio v2 - Full Stack Developer

A modern, minimalist portfolio website with a sleek dark design for full stack developers to showcase their skills and projects.

## Features

- Side navigation layout with icon-based interface
- Monochromatic black, gray, and white color scheme
- Skill bars with percentage visualization
- Custom hover effects and animations
- Responsive design for all devices
- Modern typography with monospace accents

## Technologies Used

- HTML5
- CSS3
- Tailwind CSS (via CDN)
- Google Fonts (Space Mono and Inter)
- Vanilla JavaScript

## Design Highlights

- Fixed side navigation that's always accessible
- Minimalist and focused user interface
- Subtle animations and transitions
- Border-based styling rather than shadows
- Clean typography with monospace accents for coding aesthetics

## Setup and Installation

1. Clone this repository
```
git clone https://github.com/yourusername/portfolio.git
```

2. Navigate to the v2 folder
```
cd portfolio/v2
```

3. Open `index.html` in your browser or use a local development server
```
# With Python
python -m http.server

# With Node.js
npx serve
```

## Customization

### Personal Information
Edit the HTML content in `index.html` to update:
- Your name and title
- About me description
- Work experience timeline
- Skills and proficiency levels
- Project details
- Contact information

### Profile Picture
Replace the placeholder emoji with your profile picture:

```html
<div class="w-full h-full flex items-center justify-center">
    <!-- Replace with your image -->
    <img src="path/to/your/image.jpg" alt="Your Name" class="w-full h-full object-cover">
</div>
```

### Project Images
Replace the emoji placeholders with actual project screenshots:

```html
<div class="absolute inset-0 flex items-center justify-center">
    <!-- Replace with project image -->
    <img src="path/to/project-image.jpg" alt="Project Name" class="w-full h-full object-cover">
</div>
```

### Customizing Skills
To adjust your skill proficiency, simply modify the `data-level` attribute in the skill bars:

```html
<div class="skill-bar" data-skill="React" data-level="90"></div>
```

## License

MIT © [Your Name] 