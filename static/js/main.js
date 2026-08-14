/* ============================================================
   Student Attendance System — main.js
   Vanilla JavaScript, no frameworks
   ============================================================ */

document.addEventListener('DOMContentLoaded', function () {
    var sidebar = document.getElementById('sidebar');
    var toggle = document.getElementById('sidebar-toggle');
    var overlay = document.getElementById('sidebar-overlay');

    function closeSidebar() {
        if (sidebar) sidebar.classList.remove('open');
        if (overlay) overlay.classList.remove('show');
        if (toggle) toggle.setAttribute('aria-expanded', 'false');
    }

    // Mobile sidebar toggle
    if (toggle && sidebar) {
        toggle.addEventListener('click', function () {
            var open = sidebar.classList.toggle('open');
            if (overlay) overlay.classList.toggle('show', open);
            toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
        });
    }

    if (overlay) {
        overlay.addEventListener('click', closeSidebar);
    }

    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') closeSidebar();
    });

    // Auto-dismiss Django messages
    document.querySelectorAll('.messages .alert').forEach(function (alert) {
        var close = alert.querySelector('.alert-close');
        if (close) {
            close.addEventListener('click', function () {
                alert.remove();
            });
        }

        window.setTimeout(function () {
            alert.classList.add('alert-fade');
            window.setTimeout(function () {
                alert.remove();
            }, 450);
        }, 5000);
    });

    // Client-side table search (no backend changes needed)
    document.querySelectorAll('[data-table-search]').forEach(function (input) {
        input.addEventListener('input', function () {
            var table = document.getElementById(input.getAttribute('data-table-search'));
            if (!table) return;

            var query = input.value.trim().toLowerCase();
            var rows = table.querySelectorAll('tbody tr');
            var anyVisible = false;

            rows.forEach(function (row) {
                if (row.classList.contains('no-results-row') || row.classList.contains('empty-row')) {
                    return;
                }
                var match = !query || row.textContent.toLowerCase().indexOf(query) !== -1;
                row.style.display = match ? '' : 'none';
                if (match) anyVisible = true;
            });

            var noResults = table.querySelector('.no-results-row');
            if (noResults) {
                noResults.style.display = (query && !anyVisible) ? '' : 'none';
            }
        });
    });

    // Generic confirmation for delete forms
    document.querySelectorAll('form[data-confirm]').forEach(function (form) {
        form.addEventListener('submit', function (e) {
            var message = form.getAttribute('data-confirm');
            if (!window.confirm(message)) {
                e.preventDefault();
            }
        });
    });
});
