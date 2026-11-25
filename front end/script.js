async function loadProjects() {
    const grid = document.getElementById('project_container');
    
    try {
        const response = await fetch('http://onrender.com');
        
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        
        const projects = await response.json();
        
        // Clear the "Loading..." text
        grid.innerHTML = '';

        // Loop through each project from Python and build a card
        projects.forEach(project => {
            const card = document.createElement('div');
            card.className = 'card';
            
            card.innerHTML = `
                <h3>${project.title}</h3>
                <p>${project.description}</p>
                <div class="tags">
                    ${project.tech_stack.map(tech => `<span class="tag">${tech}</span>`).join('')}
                </div>
                <div class="links">
                    <a href="${project.github_url}" target="_blank">GitHub Code</a>
                    ${project.live_url ? `<a href="${project.live_url}" target="_blank">Live Demo</a>` : ''}
                </div>
            `;
            
            grid.appendChild(card);
        });
    } catch (error) {
        grid.innerHTML = '<p style="color: #ff6b6b;">Error connecting to Python API. Make sure Uvicorn is running in your terminal!</p>';
        console.error('Fetch error:', error);
    }
}

// Run when the page loads
loadProjects();