function initializeCodeBlocks() {
    document.querySelectorAll('.copy-button').forEach(button => {
        if (!button.hasListener) {
            button.addEventListener('click', async function() {
                const codeBlock = this.closest('.code-block');
                const code = codeBlock.querySelector('code').textContent;

                try {
                    await navigator.clipboard.writeText(code);
                    
                    // Visual feedback
                    const originalText = this.textContent;
                    this.textContent = 'Copied!';
                    this.classList.add('bg-green-600');
                    
                    setTimeout(() => {
                        this.textContent = originalText;
                        this.classList.remove('bg-green-600');
                    }, 2000);
                } catch (err) {
                    console.error('Failed to copy code:', err);
                    alert('Failed to copy code to clipboard');
                }
            });
            button.hasListener = true;
        }
    });
}

document.addEventListener('DOMContentLoaded', initializeCodeBlocks);