// ========================================
// PAC Study - Centralized JavaScript Utilities
// ========================================

// Navigation Toggle Functionality
function initNavigation() {
    const navToggle = document.getElementById('navToggle');
    const navSidebar = document.getElementById('navSidebar');
    const navOverlay = document.getElementById('navOverlay');

    if (!navToggle || !navSidebar || !navOverlay) return;

    navToggle.addEventListener('click', () => {
        navSidebar.classList.toggle('active');
        navOverlay.classList.toggle('active');
        navToggle.classList.toggle('active');
    });

    navOverlay.addEventListener('click', () => {
        navSidebar.classList.remove('active');
        navOverlay.classList.remove('active');
        navToggle.classList.remove('active');
    });

    // Close sidebar when clicking a link
    navSidebar.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
            navSidebar.classList.remove('active');
            navOverlay.classList.remove('active');
            navToggle.classList.remove('active');
        });
    });
}

// School Color Mapping (for charts and tables)
const schoolColors = {
    'Cottonwood': 'rgba(220, 38, 38, 0.7)',
    'Crestview': 'rgba(234, 88, 12, 0.7)',
    'Driggs': 'rgba(202, 138, 4, 0.7)',
    'Eastwood': 'rgba(101, 163, 13, 0.7)',
    'Morningside': 'rgba(5, 150, 105, 0.7)',
    'Morningside_ALC': 'rgba(5, 150, 105, 0.7)',
    'Morningside_DLI': 'rgba(5, 150, 105, 0.7)',
    'Morningside_Traditional': 'rgba(5, 150, 105, 0.7)',
    'Oakridge': 'rgba(6, 182, 212, 0.7)',
    'Oakwood': 'rgba(59, 130, 246, 0.7)',
    'Oakwood_DLI': 'rgba(59, 130, 246, 0.7)',
    'Oakwood_Traditional': 'rgba(59, 130, 246, 0.7)',
    'Penn': 'rgba(139, 92, 246, 0.7)',
    'Penn_DLI': 'rgba(139, 92, 246, 0.7)',
    'Penn_Traditional': 'rgba(139, 92, 246, 0.7)',
    'Rosecrest': 'rgba(217, 70, 239, 0.7)',
    'Upland Terrace': 'rgba(236, 72, 153, 0.7)'
};

const defaultColor = 'rgba(107, 114, 128, 0.5)'; // Gray for other schools

function getSchoolColor(schoolName) {
    if (!schoolName) return defaultColor;

    // Check direct match
    if (schoolColors[schoolName]) {
        return schoolColors[schoolName];
    }

    // Check uppercase match
    const upperName = schoolName.toUpperCase();
    for (const [key, value] of Object.entries(schoolColors)) {
        if (key.toUpperCase() === upperName ||
            upperName.includes(key.toUpperCase()) ||
            key.toUpperCase().includes(upperName)) {
            return value;
        }
    }

    return defaultColor;
}

function getSchoolClass(schoolName) {
    if (!schoolName) return 'other';

    const upper = schoolName.toUpperCase().replace(/_/g, ' ');

    if (upper.includes('COTTONWOOD')) return 'cottonwood';
    if (upper.includes('CRESTVIEW')) return 'crestview';
    if (upper.includes('DRIGGS')) return 'driggs';
    if (upper.includes('EASTWOOD')) return 'eastwood';
    if (upper.includes('MORNINGSIDE')) return 'morningside';
    if (upper.includes('OAKRIDGE')) return 'oakridge';
    if (upper.includes('OAKWOOD')) return 'oakwood';
    if (upper.includes('PENN')) return 'penn';
    if (upper.includes('ROSECREST')) return 'rosecrest';
    if (upper.includes('UPLAND')) return 'upland';

    return 'other';
}

// CSV Parsing Utility
function parseCSV(csvText) {
    const lines = csvText.trim().split('\n');
    const headers = lines[0].split(',').slice(1); // Remove first column (boundary name)
    const data = {};

    for (let i = 1; i < lines.length; i++) {
        const values = lines[i].split(',');
        const boundary = values[0];
        data[boundary] = {};

        for (let j = 1; j < values.length; j++) {
            data[boundary][headers[j - 1]] = parseInt(values[j]) || 0;
        }
    }

    return { headers, data };
}

// Load CSV File
async function loadCSV(filePath) {
    try {
        const response = await fetch(filePath);
        const csvText = await response.text();
        return parseCSV(csvText);
    } catch (error) {
        console.error('Error loading CSV:', error);
        return null;
    }
}

// Utility to get a slugified version of the title for filenames
function slugify(text) {
    return text
        .toString()
        .toLowerCase()
        .replace(/\s+/g, '_')      // Replace spaces with _
        .replace(/[^\w\-]+/g, '')  // Remove all non-word chars
        .replace(/\_+/g, '_')      // Replace multiple _ with single _
        .replace(/^_+/, '')        // Trim _ from start of text
        .replace(/_+$/, '');       // Trim _ from end of text
}

// Create Sankey Diagram
function createSankey(elementId, csvData, title) {
    const { headers, data } = csvData;

    // Define Area 5 schools
    const area5SchoolNames = [
        'COTTONWOOD', 'CRESTVIEW', 'DRIGGS', 'EASTWOOD', 'MORNINGSIDE',
        'OAKRIDGE', 'OAKWOOD', 'PENN', 'ROSECREST', 'UPLAND TERRACE'
    ];

    // Helper function to check if a name is Area 5 related
    const isArea5 = (name) => {
        const upper = name.toUpperCase().replace(/_/g, ' ');
        return area5SchoolNames.some(school => upper.includes(school) || upper === school);
    };

    // Separate and sort boundaries: Area 5 first, then others alphabetically
    const boundaries = Object.keys(data);
    const area5Boundaries = boundaries.filter(b => isArea5(b));
    const otherBoundaries = boundaries.filter(b => !isArea5(b)).sort();
    const sortedBoundaries = [...area5Boundaries, ...otherBoundaries];

    // Separate and sort schools: Area 5 first, then others alphabetically
    const schools = headers;
    const area5Schools = schools.filter(s => isArea5(s));
    const otherSchools = schools.filter(s => !isArea5(s)).sort();
    const sortedSchools = [...area5Schools, ...otherSchools];

    // All nodes: sorted boundaries first, then sorted schools
    const nodes = [...sortedBoundaries, ...sortedSchools];
    const nodeColors = [];

    // Color boundaries based on school color if they match
    sortedBoundaries.forEach(b => {
        nodeColors.push(getSchoolColor(b.toUpperCase()));
    });

    // Color schools
    sortedSchools.forEach(s => {
        nodeColors.push(getSchoolColor(s));
    });

    // Calculate source totals for percentage calculation
    const sourceTotals = {};
    boundaries.forEach(boundary => {
        sourceTotals[boundary] = schools.reduce((sum, school) =>
            sum + (data[boundary][school] || 0), 0);
    });

    // Build links using sorted indices
    const source = [];
    const target = [];
    const value = [];
    const linkColors = [];
    const percentages = [];

    sortedBoundaries.forEach((boundary, newBIdx) => {
        sortedSchools.forEach((school, newSIdx) => {
            const count = data[boundary][school];
            if (count > 0) {
                source.push(newBIdx);
                target.push(sortedBoundaries.length + newSIdx);
                value.push(count);
                linkColors.push(getSchoolColor(school).replace('0.7', '0.3'));

                // Calculate percentage of source total
                const sourceTotal = sourceTotals[boundary] || 1;
                const percentage = sourceTotal > 0 ? (count / sourceTotal * 100) : 0;
                percentages.push(percentage);
            }
        });
    });

    // Hover template with percentage
    const hoverTemplate = '%{source.label} → %{target.label}<br><b>%{value} students</b><br>(%{customdata:.1f}% of %{source.label} total)<extra></extra>';

    const sankeyData = [{
        type: "sankey",
        orientation: "h",
        node: {
            pad: 15,
            thickness: 20,
            line: { color: "#3c4043", width: 0.5 },
            label: nodes,
            color: nodeColors,
            hovertemplate: '%{label}<br>%{value} students<extra></extra>'
        },
        link: {
            source: source,
            target: target,
            value: value,
            color: linkColors,
            customdata: percentages,
            hovertemplate: hoverTemplate
        }
    }];

    const layout = {
        title: {
            text: title,
            font: { size: 18, color: '#e8eaed' }
        },
        font: { size: 10, color: '#e8eaed' },
        paper_bgcolor: '#1a1a1a',
        plot_bgcolor: '#1a1a1a',
        margin: { l: 20, r: 20, t: 40, b: 20 },
        height: window.innerHeight - (16*6),
        autosize: true
    };

    // --- Custom: descriptive filename for chart download ---
    let filename = "pac_study_sankey";
    if (title && typeof title === 'string') {
        filename = slugify(title);
    }

    Plotly.newPlot(elementId, sankeyData, layout, {
        responsive: true,
        toImage: {
            filename: filename
        }
    });
}

// Create Matrix Table
function createMatrixTable(tableId, csvData) {
    const { headers, data } = csvData;
    const boundaries = Object.keys(data);
    const table = document.getElementById(tableId);

    if (!table) return;

    // Calculate column totals
    const columnTotals = {};
    headers.forEach(school => {
        columnTotals[school] = boundaries.reduce((sum, boundary) => {
            return sum + (data[boundary][school] || 0);
        }, 0);
    });

    // Create header row
    let html = '<thead><tr><th class="boundary-header">From Boundary (Rows) \\ To School (Columns)</th>';
    headers.forEach(school => {
        html += `<th class="${getSchoolClass(school)}">${school.replace(/_/g, ' ')}</th>`;
    });
    html += '<th style="background: var(--bg-tertiary); font-weight: bold;">Row Total</th>';
    html += '</tr></thead><tbody>';

    // Create data rows
    boundaries.forEach(boundary => {
        const boundaryUpper = boundary.toUpperCase();
        const schoolClass = getSchoolClass(boundaryUpper);

        html += `<tr><td class="boundary-cell ${schoolClass}">${boundary}</td>`;

        // Calculate row total
        let rowTotal = 0;

        headers.forEach(school => {
            const count = data[boundary][school];
            rowTotal += count;
            const cellClass = getSchoolClass(school);

            // Check if diagonal (same boundary and school)
            const isDiagonal = boundaryUpper === school.toUpperCase().replace(/_/g, ' ');

            let classes = `${cellClass}`;
            if (isDiagonal) classes += ' diagonal';
            if (count === 0) classes += ' zero';

            html += `<td class="${classes}">${count}</td>`;
        });

        // Add row total
        html += `<td style="font-weight: bold; background: var(--bg-tertiary);">${rowTotal}</td>`;
        html += '</tr>';
    });

    // Add column totals row
    html += '<tr style="background: var(--bg-tertiary);"><td class="boundary-cell" style="font-weight: bold; background: var(--bg-tertiary);">Column Total</td>';
    
    let grandTotal = 0;
    headers.forEach(school => {
        const total = columnTotals[school];
        grandTotal += total;
        html += `<td style="font-weight: bold;">${total}</td>`;
    });
    
    // Grand total cell
    html += `<td style="font-weight: bold; background: var(--accent-cyan); color: #000;">${grandTotal}</td>`;
    html += '</tr>';

    html += '</tbody>';
    table.innerHTML = html;
}

// Initialize on DOM load
document.addEventListener('DOMContentLoaded', () => {
    initNavigation();
});
