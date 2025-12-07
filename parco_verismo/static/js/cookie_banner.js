// Cookie Banner GDPR - Parco Letterario del Verismo
// Gestione consenso cookie conforme normativa italiana

(function() {
    'use strict';

    const COOKIE_NAME = 'cookie_consent';
    const COOKIE_DURATION = 365; // giorni

    // Funzioni helper per cookie
    function setCookie(name, value, days) {
        const date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        const expires = "expires=" + date.toUTCString();
        document.cookie = name + "=" + value + ";" + expires + ";path=/;SameSite=Lax";
    }

    function getCookie(name) {
        const nameEQ = name + "=";
        const ca = document.cookie.split(';');
        for(let i = 0; i < ca.length; i++) {
            let c = ca[i];
            while (c.charAt(0) === ' ') c = c.substring(1, c.length);
            if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
        }
        return null;
    }

    function saveConsent(preferences) {
        const consent = JSON.stringify(preferences);
        setCookie(COOKIE_NAME, consent, COOKIE_DURATION);
        
        // Applica le preferenze
        applyConsent(preferences);
        
        // Nascondi banner
        hideBanner();
    }

    function applyConsent(preferences) {
        // Cookie tecnici sempre attivi (necessari per il funzionamento)
        // Non serve fare nulla

        // Cookie analytics
        if (preferences.analytics) {
            enableAnalytics();
        } else {
            disableAnalytics();
        }

        // Cookie marketing/social
        if (preferences.marketing) {
            enableMarketing();
        } else {
            disableMarketing();
        }
    }

    function enableAnalytics() {
        // Esempio: attiva Google Analytics o Matomo
        console.log('Analytics cookies enabled');
        // window.gtag('consent', 'update', {'analytics_storage': 'granted'});
        
        // Se usi Matomo (consigliato per PA):
        // _paq.push(['setConsentGiven']);
    }

    function disableAnalytics() {
        console.log('Analytics cookies disabled');
        // window.gtag('consent', 'update', {'analytics_storage': 'denied'});
        
        // Se usi Matomo:
        // _paq.push(['forgetConsentGiven']);
    }

    function enableMarketing() {
        console.log('Marketing cookies enabled');
        // Attiva script marketing/social se necessari
    }

    function disableMarketing() {
        console.log('Marketing cookies disabled');
        // Disattiva script marketing/social
    }

    function showBanner() {
        const banner = document.getElementById('cookie-banner');
        if (banner) {
            banner.classList.add('show');
        }
    }

    function hideBanner() {
        const banner = document.getElementById('cookie-banner');
        const modal = document.getElementById('cookie-preferences-modal');
        if (banner) banner.classList.remove('show');
        if (modal) modal.classList.remove('show');
    }

    function showPreferencesModal() {
        const modal = document.getElementById('cookie-preferences-modal');
        if (modal) {
            modal.classList.add('show');
        }
    }

    function hidePreferencesModal() {
        const modal = document.getElementById('cookie-preferences-modal');
        if (modal) {
            modal.classList.remove('show');
        }
    }

    function getPreferencesFromModal() {
        return {
            necessary: true, // Sempre true
            analytics: document.getElementById('analytics-cookies')?.checked || false,
            marketing: document.getElementById('marketing-cookies')?.checked || false
        };
    }

    // Inizializzazione
    function init() {
        // Controlla se l'utente ha già dato il consenso
        const consent = getCookie(COOKIE_NAME);
        
        if (!consent) {
            // Mostra banner se non c'è consenso
            showBanner();
        } else {
            // Applica preferenze salvate
            try {
                const preferences = JSON.parse(consent);
                applyConsent(preferences);
            } catch (e) {
                // Se c'è un errore, mostra di nuovo il banner
                showBanner();
            }
        }

        // Event listeners
        const acceptAllBtn = document.getElementById('accept-all-cookies');
        const acceptNecessaryBtn = document.getElementById('accept-necessary-cookies');
        const customizeBtn = document.getElementById('customize-cookies');
        const savePreferencesBtn = document.getElementById('save-preferences');
        const closeModalBtn = document.querySelector('.cookie-modal-close');

        if (acceptAllBtn) {
            acceptAllBtn.addEventListener('click', function() {
                saveConsent({
                    necessary: true,
                    analytics: true,
                    marketing: true
                });
            });
        }

        if (acceptNecessaryBtn) {
            acceptNecessaryBtn.addEventListener('click', function() {
                saveConsent({
                    necessary: true,
                    analytics: false,
                    marketing: false
                });
            });
        }

        if (customizeBtn) {
            customizeBtn.addEventListener('click', function() {
                showPreferencesModal();
            });
        }

        if (savePreferencesBtn) {
            savePreferencesBtn.addEventListener('click', function() {
                const preferences = getPreferencesFromModal();
                saveConsent(preferences);
                hidePreferencesModal();
            });
        }

        if (closeModalBtn) {
            closeModalBtn.addEventListener('click', function() {
                hidePreferencesModal();
            });
        }

        // Chiudi modal cliccando fuori
        const modal = document.getElementById('cookie-preferences-modal');
        if (modal) {
            modal.addEventListener('click', function(e) {
                if (e.target === modal) {
                    hidePreferencesModal();
                }
            });
        }
    }

    // Avvia quando il DOM è pronto
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    // Esponi funzione globale per riaprire le preferenze
    window.reopenCookiePreferences = function() {
        showPreferencesModal();
    };

})();
